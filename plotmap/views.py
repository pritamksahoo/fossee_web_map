from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from .models import csvfile
import pandas as pd
import numpy as np
from pathlib import Path
import os
from fuzzywuzzy import fuzz, process
from django.http import JsonResponse
from django.http import Http404

def home(request):
    return render(request, 'home.html')


def upload_file(request):
	'''Uploading file and creating file object'''
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES["myfile"]
		try:
		    newfile = csvfile.objects.create(fileobject=myfile)  
		    newfile.save()
		    return redirect('analyze', pk=newfile.id)
		except:
			raise Http404
			return redirect('home')
	else:
		return redirect('home')


def analyze(request, pk):
    '''Printing original data'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    data = pd.read_csv(str(file))
    cols = data.columns.tolist()
    col1 = process.extractOne('STATE', cols, scorer=fuzz.WRatio)[0]
    col2 = process.extractOne('DISTRICT', cols, scorer=fuzz.WRatio)[0]
    col3 = process.extractOne('COLLEGE NAME', cols, scorer=fuzz.WRatio)[0]
    data = data.rename({col1: 'STATE', col2: 'DISTRICT', col3: 'COLLEGE NAME'}, axis='columns')
    cols = data.columns.tolist()
    temp = []
    for i in cols:
    	if i != 'STATE' and i != 'DISTRICT' and i != 'COLLEGE NAME':
    		temp.append(i)
    del temp[0]
    cols = ['STATE','DISTRICT','COLLEGE NAME'] + temp
    data = data[cols]
    data['STATE'] = data['STATE'].str.upper()
    data['DISTRICT'] = data['DISTRICT'].str.upper()
    data['COLLEGE NAME'] = data['COLLEGE NAME'].str.upper()
    data.to_csv(str(file))
    '''Determining which page to show'''
    if len(data) > 4000 and len(data) <= 6000:
        return redirect('groupby_district', pk=pk)
    elif len(data) > 6000:
        return redirect('groupby_state', pk=pk)
    else:
        return redirect('showdata', pk=pk)


def showdata(request, pk):
    '''Showing full data'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    data = pd.read_csv(str(file))
    data = data[data.columns.tolist()[1:]]
    return render(request, 'prelemdata.html', {'fileid': pk, 'orgdata': data.to_html(), 'map': 'no'})


def groupby_district(request, pk):
    '''printing grouped data (state, district, and no. of colleges only)'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    data = pd.read_csv(str(file))
    data['COLLEGE'] = data['COLLEGE NAME']
    data = data.groupby(['STATE', 'DISTRICT'], as_index=False).count()  #Grouping by state and district
    col = list(data)
    for c in col:
	    if c != 'COLLEGE' and c != 'STATE' and c != 'DISTRICT':
	        del data[c]
    return render(request, 'nicedata.html', {'fileid': pk, 'orgdata': data.to_html(), 'map': 'no'})


def groupby_state(request, pk):
    '''printing grouped data (state, district, and no. of colleges only)'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    data = pd.read_csv(str(file))
    data['COLLEGE'] = data['COLLEGE NAME']
    data = data.groupby('STATE', as_index=False).count()  #Grouping by state and district
    col = list(data)
    for c in col:
        if c != 'COLLEGE' and c != 'STATE':
            del data[c]
    ''' For India map plot'''
    india_map = [
        ['State Code', 'State', 'No. of colleges'],
        ["IN-AP", "Andhra Pradesh", 0],
        ["IN-AR", "Arunachal Pradesh", 0],
        ["IN-AS", "Assam", 0],
        ["IN-BR", "Bihar", 0],
        ["IN-CT", "Chhattisgarh", 0],
        ["IN-GA", "Goa", 0],
        ["IN-GJ", "Gujarat", 0],
        ["IN-HR", "Haryana", 0],
        ["IN-HP", "Himachal Pradesh", 0],
        ["IN-JK", "Jammu and Kashmir", 0],
        ["IN-JH", "Jharkhand", 0],
        ["IN-KA", "Karnataka", 0],
        ["IN-KL", "Kerala", 0],
        ["IN-MP", "Madhya Pradesh", 0],
        ["IN-MH", "Maharashtra", 0],
        ["IN-MN", "Manipur", 0],
        ["IN-ML", "Meghalaya", 0],
        ["IN-MZ", "Mizoram", 0],
        ["IN-NL", "Nagaland", 0],
        ["IN-OR", "Odisha", 0],
        ["IN-PB", "Punjab", 0],
        ["IN-RJ", "Rajasthan", 0],
        ["IN-SK", "Sikkim", 0],
        ["IN-TN", "Tamil Nadu", 0],
        ["IN-TG", "Telangana", 0],
        ["IN-TR", "Tripura", 0],
        ["IN-UT", "Uttarakhand", 0],
        ["IN-UP", "Uttar Pradesh", 0],
        ["IN-WB", "West Bengal", 0],
        ["IN-AN", "Andaman and Nicobar Islands", 0],
        ["IN-CH", "Chandigarh", 0],
        ["IN-DN", "Dadra and Nagar Haveli", 0],
        ["IN-DD", "Daman and Diu", 0],
        ["IN-DL", "Delhi", 0],
        ["IN-LD", "Lakshadweep", 0],
        ["IN-PY", "Puducherry", 0]
    ]
    choices = list()
    final = list()
    '''Counting stats for individual states for plotting'''
    for l in india_map:
        choices.append(l[1])
    for item in data['STATE']:
        key = item
        final.append(process.extractOne(key, choices, scorer=fuzz.WRatio)[0])
    data['STATE'] = final
    for s,c in list(zip(data['STATE'], data['COLLEGE'])):
        for i in india_map:
            if i[1] == s:
                i[2] += int(c)
    india_map_pie = []
    for info in india_map:
        india_map_pie.append([info[1], info[2]])
    return render(request, 'nicedata.html', {'fileid': pk, 'orgdata': data.to_html(), 'map': 'yes', 'state_list': india_map, 'pie_list': india_map_pie})


def groupby_college(request, pk):
    '''printing grouped data (state, district, and no. of colleges only)'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    data = pd.read_csv(str(file))
    data['Stat/college'] = data['COLLEGE NAME']
    data = data.groupby(['STATE', 'DISTRICT', 'COLLEGE NAME'], as_index=False).count()  #Grouping by state and district
    col = list(data)
    for c in col:
        if c != 'COLLEGE NAME' and c != 'STATE' and c != 'DISTRICT' and c != 'Stat/college':
            del data[c]
    return render(request, 'nicedata.html', {'fileid': pk, 'orgdata': data.to_html(), 'map': 'no'})


def clean_data(request, pk):
    '''Cleaning NaN entries and dropping duplicate rows'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    data = pd.read_csv(str(file))
    '''Dropping values for null (NaN) entries for COLLEGES'''
    data = data.dropna(subset=['COLLEGE NAME'])
    '''Dropping duplicate rows'''
    cols = data.columns.tolist()
    del cols[0]
    data = data.drop_duplicates(cols, keep='first')
    data.to_csv(str(file), index=False)
    return render(request, 'cleandata.html', {'fileid': pk})


def modify_data(request, pk):
    '''Checking errors and giving suggestions'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404

    data = pd.read_csv(str(file))
    temp_data = pd.read_csv(str(file))
    data = data[data.columns.tolist()[1:4]]
    data['error'] = 'no'
    ref_data = pd.read_csv("files/college.csv")
    list_of_state = list(set(ref_data['STATE'].str.upper()))
    list_of_district = list(set(ref_data['DISTRICT'].str.upper()))
    list_of_college = list(ref_data['COLLEGE NAME'].str.upper())
    for i in range(len(data)):
        '''If State data is wrong'''
        if data.loc[i].isnull()['STATE'] == False and data.loc[i]['STATE'].upper() not in list_of_state:
            match = process.extractOne(data.loc[i][0], list_of_state, scorer=fuzz.WRatio)
            if int(match[1]) > 80:
                data.loc[i][0] = str(match[0])
            else:
                data.loc[i][0] = np.nan
        '''If state is null still, fill that w.r.t. corresponding college'''
        if data.loc[i].isnull()['STATE'] == True:
            if str(data.loc[i][2]) in list_of_college:
                ind = list_of_college.index(data.loc[i][2])
                data['temp'] = data.index
                temp_data['temp'] = temp_data.index
                data.loc[data['temp'] == i, 'STATE'] = (ref_data.loc[ind]['STATE']).upper()
                temp_data.loc[temp_data['temp'] == i, 'STATE'] = (ref_data.loc[ind]['STATE']).upper()
                del data['temp']
                del temp_data['temp']
                temp_data.to_csv(str(file))

        '''If District is wrong'''
        if data.loc[i].isnull()['DISTRICT'] == False and data.loc[i][1].upper() not in list_of_district:
            if data.loc[i].isnull()['STATE'] == False:
                list_ref_district = list(map(lambda x:x.upper(), list(ref_data['DISTRICT'][ref_data['STATE'].str.upper() == str(data.loc[i][0]).upper()])))
                match = process.extractOne(data.loc[i]['DISTRICT'], list_ref_district, scorer=fuzz.WRatio)
                if(match):
                    if int(match[1]) > 80:
                        data.loc[i][1] = str(match[0])
                    else:
                        data.loc[i][1] = np.nan
            else:
                list_ref_district = list(map(lambda x:x.upper(), list(ref_data['DISTRICT'])))
                match = process.extractOne(data.loc[i][1], list_ref_district, scorer=fuzz.WRatio)
                if int(match[1]) > 80:
                    data.loc[i][1] = str(match[0])
                else:
                    data.loc[i][1] = np.nan

        '''Checking College data'''
        if str(data.loc[i][2]) not in list_of_college:
            data.loc[i]['error'] = 'yes'
            if data.loc[i].isnull()['STATE'] == False:
                list_ref_college = list(map(lambda x:x.upper(), list(ref_data['COLLEGE NAME'][ref_data['STATE'].str.upper() == str(data.loc[i][0]).upper()])))
            else:
                list_ref_college = list_of_college
            
            #print(list_ref_college)
            match = process.extract(str(data.loc[i][2]), list_ref_college, scorer=fuzz.WRatio)
            first = int(match[0][1])
            for j in range(len(match)):
                if first-int(match[j][1]) > 5:
                    break
            match = match[:j+1]
            match1 = []
            #print(match)
            '''abbreviation matching'''
            if len(str(data.loc[i][2])) <= 10 and len(str(data.loc[i][2]).split()) <= 2:
                for j in range(len(list_ref_college)):
                    temp = ''.join(w[0].upper() for w in list_ref_college[j].split())
                    ratio = fuzz.ratio(str(data.loc[i][2]), temp.upper())
                    match1.append((list_ref_college[j], ratio))
                match1 = sorted(match1, key=lambda x: x[1], reverse=True)
                first = int(match1[0][1])
                for j in range(len(match1)):
                    if first-int(match1[j][1]) > 5:
                        break
                match1 = match1[:j+1]
                final = match1
            else:
                final = match
            final = sorted(final, key = lambda x: x[1], reverse=True)
            #print(final)
            result = []
            result.append(data.loc[i][2])
            for j in range(len(final)):
                result.append(final[j][0])
            data.loc[i][2] = result
            #print(data.loc[i][2])
    data['pos'] = data.index
    #data.to_csv(str(file))
    return render(request, 'moddata.html', {'fileid': pk, 'orgdata': data, 'map': 'no'})


def search(request, pk):
    '''Search by college name'''
    if request.is_ajax():
        name = request.GET.get('searchText', None)
        name = name.upper()
        file = csvfile.objects.get(id=pk)
        data = pd.read_csv(str(file))
        college_list = list(set(data['COLLEGE NAME']))
        result = []
        # Fuzzy logic for matching strings
        leng = len(name.split())
        res = []
        for i in range(len(college_list)):
            temp = ' '.join(str(college_list[i]).split()[:leng+1])
            ratio = fuzz.ratio(name, temp.upper())
            res.append((college_list[i], ratio))
        res = sorted(res, key=lambda x: x[1], reverse=True)
        final_res = []
        first = res[0][1]
        for i in range(len(res)):
            if (first - res[i][1]) <= 10:
                final_res.append(res[i])
            else:
                break
        
        '''counting sum of characters (excluding white spaces) in search query'''
        summ = len(name) - len(name.split()) + 1 
        
        ''' String searching for abbreviation'''
        if (summ <= 5) and (len(name.split()) == 1 or summ-len(name.split()) < 2):
            res1 = []
            for i in range(len(college_list)):
                temp = ''
                for w in str(college_list[i]).split():
                    if w != 'AND' and w != 'OF' and w != 'THE':
                        temp = temp + w[0].upper()
                if(len(temp) >= summ):
                    temp = temp[:summ+1]
                    ratio = fuzz.ratio(name, temp.upper())                            # For abbreviation matching
                    res1.append((college_list[i], ratio))
            res1 = sorted(res1, key=lambda x: x[1], reverse=True)
            final_res1 = []
            first1 = res1[0][1]
            for i in range(len(res1)):
                if (first1 - res1[i][1]) <= 10:
                    final_res1.append(res1[i])
                else:
                    break
            merge_res = final_res + final_res1
        else:
            merge_res = final_res
        
        merge_res = sorted(merge_res, key = lambda x: x[1], reverse=True)
        
        first = merge_res[0][1]
        '''applying certain conditions on search result'''
        if first > 50:
            for i in range(len(merge_res)):
                if merge_res[i][0] not in result:
                    result.append(merge_res[i][0])
        if len(result) > 20 and first <= 30:
            result.clear()
        #print(result)
        
        data = {
            'search_result': result
        }
        return JsonResponse(data)


def save_changes(request, pk):
    '''Make final change in file according to user's choice in 'modify data' page '''
    if request.is_ajax():
        text = request.GET.get('text', None)
        index = int(request.GET.get('index', None))
        #print(text, index)
        try:
            file = csvfile.objects.get(id=pk)
        except csvfile.DoesNotExist:
            raise Http404

        ref_data = pd.read_csv('files/college.csv')
        data = pd.read_csv(str(file))
        data['temp'] = data.index
        data.loc[data['temp'] == index, 'COLLEGE NAME'] = str(text)
        #For invalid state
        if data.loc[index].isnull()['STATE'] == True:
            ref_state = ref_data.loc[ref_data[ref_data['COLLEGE NAME'] == str(text)].index.values.astype(int)[0]]['STATE']
            data.loc[data['temp'] == index, 'STATE'] = ref_state
        del data['temp']
        #print(data.loc[index]['STATE'])
        cols = data.columns.tolist()
        del cols[0]
        data = data[cols]
        data.to_csv(str(file))
        data = {
            'text': text
        }
        return JsonResponse(data)


def close(request, pk):
    '''Deleting all existing records regarding user's file'''
    try:
        file = csvfile.objects.get(id=pk)
    except csvfile.DoesNotExist:
        raise Http404
    file.delete()
    os.remove(str(file))
    #csvfile.objects.get(id=pk).delete()
    return redirect('home')
