# coding=utf-8
import os
from django.conf import settings
from django.test import TestCase, Client
from ntc.data_saver import NTCDataSaver
from ntc.models import ParsedNTC


class DataSaverTests(TestCase):
    def setUp(self):
        json_path = os.path.join("ntc", "test_data", "data.json")
        json_file = open(json_path, 'rb')
        self.json = json_file.read()

    def test_data_saved_first_object(self):
        data_saver = NTCDataSaver(self.json)
        data_saver.load()

        first_record = ParsedNTC.objects.first()
        actual_first_record_full_name = first_record.full_name
        actual_first_record_school_title = first_record.school_title
        actual_first_record_location = first_record.location
        actual_first_record_eng_lang_result = first_record.eng_lang
        actual_first_record_history_result = first_record.history

        expected_first_record_full_name = u"АБДЫКЕРИМОВ ЭЛЬНУР"
        expected_first_record_school_title = u"Абитуриент"
        expected_first_record_location = u"г. Бишкек г. БишкекНЦТ"
        expected_first_record_eng_lang_result = '22'
        expected_first_record_history_result = '29'

        self.assertEqual(actual_first_record_full_name, expected_first_record_full_name)
        self.assertEqual(actual_first_record_school_title, expected_first_record_school_title)
        self.assertEqual(actual_first_record_location, expected_first_record_location)
        self.assertEqual(actual_first_record_eng_lang_result, expected_first_record_eng_lang_result)
        self.assertEqual(actual_first_record_history_result, expected_first_record_history_result)

    def test_data_saved_last_object(self):
        data_saver = NTCDataSaver(self.json)
        data_saver.load()

        last_record = ParsedNTC.objects.last()
        actual_last_record_full_name = last_record.full_name
        actual_last_record_school_title = last_record.school_title
        actual_last_record_location = last_record.location
        actual_last_record_eng_lang_result = last_record.eng_lang
        actual_last_record_history_result = last_record.history

        expected_last_record_full_name = u"ЯКОВЛЕВА АНАСТАСИЯ"
        expected_last_record_school_title = u"Эврика"
        expected_last_record_location = u"г. Бишкек г. БишкекНЦТ"
        expected_last_record_eng_lang_result = '25'
        expected_last_record_history_result = '20'

        self.assertEqual(actual_last_record_full_name, expected_last_record_full_name)
        self.assertEqual(actual_last_record_school_title, expected_last_record_school_title)
        self.assertEqual(actual_last_record_location, expected_last_record_location)
        self.assertEqual(actual_last_record_eng_lang_result, expected_last_record_eng_lang_result)
        self.assertEqual(actual_last_record_history_result, expected_last_record_history_result)


class NTCApiViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        json_path = os.path.join("ntc", "test_data", "data.json")
        json_file = open(json_path, 'rb')
        self.json = json_file.read()

    def test_data_added(self):
        response = self.client.post(path='/api/ntc/', data=self.json, content_type="application/json", AUTHORIZATION=settings.API_KEY)

        actual_status_code = response.status_code
        expected_status_code = 200

        actual_response_content = response.content
        expected_response_content = '{"status": "ok"}'

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertEqual(actual_response_content, expected_response_content)

        first_record = ParsedNTC.objects.first()
        actual_first_record_full_name = first_record.full_name
        actual_first_record_school_title = first_record.school_title
        actual_first_record_location = first_record.location
        actual_first_record_eng_lang_result = first_record.eng_lang
        actual_first_record_history_result = first_record.history

        expected_first_record_full_name = u"АБДЫКЕРИМОВ ЭЛЬНУР"
        expected_first_record_school_title = u"Абитуриент"
        expected_first_record_location = u"г. Бишкек г. БишкекНЦТ"
        expected_first_record_eng_lang_result = '22'
        expected_first_record_history_result = '29'

        self.assertEqual(actual_first_record_full_name, expected_first_record_full_name)
        self.assertEqual(actual_first_record_school_title, expected_first_record_school_title)
        self.assertEqual(actual_first_record_location, expected_first_record_location)
        self.assertEqual(actual_first_record_eng_lang_result, expected_first_record_eng_lang_result)
        self.assertEqual(actual_first_record_history_result, expected_first_record_history_result)

    def test_unauthorized_access(self):
        response = self.client.post(path='/api/ntc/', data=self.json, content_type="application/json")

        actual_status_code = response.status_code
        expected_status_code = 401

        actual_response_content = response.content
        expected_response_content = '{"error": "wrong api key"}'

        self.assertEqual(actual_status_code, expected_status_code)
        self.assertEqual(actual_response_content, expected_response_content)
