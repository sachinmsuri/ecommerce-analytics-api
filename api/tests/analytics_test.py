import unittest
from .. import create_app
from ..config.config import config_dict
from ..utils import db
from ..upload_data import upload_data
from flask import json
import os
import io

class TestCase(unittest.TestCase):
    """
    A class to test the summary analytics 
    GET end-point '/daily/<string:date>' within 
    the analytics_namespace.

    Methods
    -------
    setUp:
        set up new test instance of Flask App
    tearDown:
        Tear down test instance of Flask App
    analytics:
        test analytics value are correct for given day
    incorrect_data:
        test when user enters date with incorrect format
    """

    def setUp(self):
        """
        Create new instance of Flask App with an 
        in-memory database.

        Upload data from data directory to in-memory
        database.

        Returns
        -------
        None
        
        """
        self.app = create_app(config=config_dict['TEST'])
        self.appctx=self.app.app_context()

        self.appctx.push()

        self.client=self.app.test_client()

        db.create_all()

        upload_data(f"sqlite://")
    
    def tearDown(self):
        """
        tear down new instance of Flask App a
        and delete in-memory database.

        Returns
        -------
        None
        
        """
        db.drop_all()

        self.appctx.pop()

        self.app=None

        self.client=None
      
    def test_analytics(self):
        """
        Test analytics/daily/<date> end-point to
        see if correct status code is returned and 
        expected anlytics is returned

        Returns
        -------
        None
        
        """
        r = self.client.get(
            'analytics/daily/2019-08-01'
        )

        rjson = json.loads(r.text)
        print(rjson)

        assert r.status_code == 200
        assert rjson['customers'] == 9
        assert rjson['quantity'] == 2895
        assert rjson['total_discount_amount'] == 130429980
        assert rjson['commissions']['Total'] == 20833236
        assert rjson['commissions']['promotions']['2'] == 188049


    def test_date_format(self):
        r = self.client.get(
            'analytics/daily/201-02-20'
        )

        assert r.status_code == 400