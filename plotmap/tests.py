from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import csvfile
from django.urls import resolve
from .views import home, upload_file, analyze, showdata, groupby_district, groupby_state, groupby_college, clean_data, modify_data, search, save_changes, close

# Create your tests here.
class HomeTests(TestCase):
    def setUp(self):
        self.csvfile = csvfile.objects.create(fileobject='files/college.csv')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)


class ShowDataTests(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_showdata_view_success_status_code(self):
        url = reverse('showdata', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_showdata_view_not_found_status_code(self):
        url = reverse('showdata', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_showdata_url_resolves_showdata_view(self):
        view = resolve('/your_file/showdata/1/')
        self.assertEquals(view.func, showdata)

    def test_showdata_view_contains_navigation_links(self):
        showdata_url = reverse('showdata', kwargs={'pk': 1})
        groupby_district_url = reverse('groupby_district', kwargs={'pk': 1})
        clean_data_url = reverse('clean_data', kwargs={'pk': 1})
        modify_data_url = reverse('modify_data', kwargs={'pk': 1})
        close_url = reverse('close', kwargs={'pk': 1})

        response = self.client.get(showdata_url)

        self.assertContains(response, 'href="{0}"'.format(groupby_district_url))
        self.assertContains(response, 'href="{0}"'.format(clean_data_url))
        self.assertContains(response, 'href="{0}"'.format(modify_data_url))
        self.assertContains(response, 'href="{0}"'.format(close_url))


class GroupbyDistrict(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_groupby_district_view_success_status_code(self):
        url = reverse('groupby_district', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 

    def test_groupby_district_view_not_found_status_code(self):
        url = reverse('groupby_district', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_groupby_district_url_resolves_showdata_view(self):
        view = resolve('/your_file/groupby_district/1/')
        self.assertEquals(view.func, groupby_district)

    def test_groupby_district_view_contains_navigation_links(self):
        showdata_url = reverse('showdata', kwargs={'pk': 1})
        groupby_district_url = reverse('groupby_district', kwargs={'pk': 1})
        clean_data_url = reverse('clean_data', kwargs={'pk': 1})
        modify_data_url = reverse('modify_data', kwargs={'pk': 1})
        groupby_state_url = reverse('groupby_state', kwargs={'pk': 1})
        groupby_college_url = reverse('groupby_college', kwargs={'pk': 1})
        close_url = reverse('close', kwargs={'pk': 1})

        response = self.client.get(groupby_district_url)

        self.assertContains(response, 'href="{0}"'.format(showdata_url))
        self.assertContains(response, 'href="{0}"'.format(clean_data_url))
        self.assertContains(response, 'href="{0}"'.format(modify_data_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_state_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_college_url))
        self.assertContains(response, 'href="{0}"'.format(close_url))


class GroupbyState(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_groupby_state_view_success_status_code(self):
        url = reverse('groupby_state', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 

    def test_groupby_state_view_not_found_status_code(self):
        url = reverse('groupby_state', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_groupby_state_url_resolves_showdata_view(self):
        view = resolve('/your_file/groupby_state/1/')
        self.assertEquals(view.func, groupby_state)

    def test_groupby_state_view_contains_navigation_links(self):
        showdata_url = reverse('showdata', kwargs={'pk': 1})
        groupby_district_url = reverse('groupby_district', kwargs={'pk': 1})
        clean_data_url = reverse('clean_data', kwargs={'pk': 1})
        modify_data_url = reverse('modify_data', kwargs={'pk': 1})
        groupby_state_url = reverse('groupby_state', kwargs={'pk': 1})
        groupby_college_url = reverse('groupby_college', kwargs={'pk': 1})
        close_url = reverse('close', kwargs={'pk': 1})

        response = self.client.get(groupby_state_url)

        self.assertContains(response, 'href="{0}"'.format(showdata_url))
        self.assertContains(response, 'href="{0}"'.format(clean_data_url))
        self.assertContains(response, 'href="{0}"'.format(modify_data_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_district_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_college_url))
        self.assertContains(response, 'href="{0}"'.format(close_url))


class GroupbyCollege(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_groupby_college_view_success_status_code(self):
        url = reverse('groupby_college', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 

    def test_groupby_college_view_not_found_status_code(self):
        url = reverse('groupby_college', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_groupby_college_url_resolves_showdata_view(self):
        view = resolve('/your_file/groupby_college/1/')
        self.assertEquals(view.func, groupby_college)

    def test_groupby_state_view_contains_navigation_links(self):
        showdata_url = reverse('showdata', kwargs={'pk': 1})
        groupby_district_url = reverse('groupby_district', kwargs={'pk': 1})
        clean_data_url = reverse('clean_data', kwargs={'pk': 1})
        modify_data_url = reverse('modify_data', kwargs={'pk': 1})
        groupby_state_url = reverse('groupby_state', kwargs={'pk': 1})
        groupby_college_url = reverse('groupby_college', kwargs={'pk': 1})
        close_url = reverse('close', kwargs={'pk': 1})

        response = self.client.get(groupby_college_url)

        self.assertContains(response, 'href="{0}"'.format(showdata_url))
        self.assertContains(response, 'href="{0}"'.format(clean_data_url))
        self.assertContains(response, 'href="{0}"'.format(modify_data_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_district_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_state_url))
        self.assertContains(response, 'href="{0}"'.format(close_url))


class CleanData(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_clean_data_view_success_status_code(self):
        url = reverse('clean_data', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 

    def test_clean_data_view_not_found_status_code(self):
        url = reverse('clean_data', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_clean_data_url_resolves_showdata_view(self):
        view = resolve('/your_file/clean_data/1/')
        self.assertEquals(view.func, clean_data)


class ModifyData(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_modify_data_view_success_status_code(self):
        url = reverse('modify_data', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200) 

    def test_modify_data_view_not_found_status_code(self):
        url = reverse('modify_data', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_modify_data_url_resolves_showdata_view(self):
        view = resolve('/your_file/modify_data/1/')
        self.assertEquals(view.func, modify_data)

    def test_groupby_state_view_contains_navigation_links(self):
        showdata_url = reverse('showdata', kwargs={'pk': 1})
        groupby_district_url = reverse('groupby_district', kwargs={'pk': 1})
        clean_data_url = reverse('clean_data', kwargs={'pk': 1})
        modify_data_url = reverse('modify_data', kwargs={'pk': 1})
        close_url = reverse('close', kwargs={'pk': 1})

        response = self.client.get(modify_data_url)

        self.assertContains(response, 'href="{0}"'.format(showdata_url))
        self.assertContains(response, 'href="{0}"'.format(clean_data_url))
        self.assertContains(response, 'href="{0}"'.format(groupby_district_url))
        self.assertContains(response, 'href="{0}"'.format(close_url))


class Analyze(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_analyze_view_success_status_code(self):
        url = reverse('analyze', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302) 

    def test_analyze_view_not_found_status_code(self):
        url = reverse('analyze', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_analyze_url_resolves_showdata_view(self):
        view = resolve('/your_file/analyze/1/')
        self.assertEquals(view.func, analyze)


class UploadFile(TestCase):
    def setUp(self):
        csvfile.objects.create(fileobject='files/college.csv')

    def test_upload_file_view_success_status_code(self):
        url = reverse('upload_file')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)  

    def test_upload_file_url_resolves_showdata_view(self):
        view = resolve('/upload_file/')
        self.assertEquals(view.func, upload_file)	


class Close(TestCase):
    def setUp(self):
        f = open('files/sample.csv', 'w')
        csvfile.objects.create(fileobject='files/sample.csv')
        f.close()

    def test_close_view_success_status_code(self):
        url = reverse('close', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302) 

    def test_close_view_not_found_status_code(self):
        url = reverse('close', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)  

    def test_close_url_resolves_showdata_view(self):
        view = resolve('/close/1/')
        self.assertEquals(view.func, close)