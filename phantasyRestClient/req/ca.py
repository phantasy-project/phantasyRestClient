#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Request for resources from ca (Channel Access) router.
"""
import json


class CAResources:
    SESSION = None
    URL = None

    def __init__(self):
        pass

    @staticmethod
    def caget(pvname: str, datatype: str):
        """Return the value of *pvname*.
        """
        r = CAResources.SESSION.get(
            f"{CAResources.URL}/epics/caget",
            params={
                'pvname': pvname,
                'datatype': datatype
                })
        if not r.ok:
            return None
        return r.json()
