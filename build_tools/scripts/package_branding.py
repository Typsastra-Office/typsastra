#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Typsastra packaging identity. Injected by build_tools/make_package.py in
# place of the default scripts/package_branding.py.

import package_utils as utils

onlyoffice = False
company_name = "Typsastra"
company_name_l = company_name.lower()
publisher_name = "Typsastra"
cert_name = "Typsastra"

s3_bucket = ""
s3_region = ""
s3_base_url = ""

if utils.is_windows():
  desktop_product_name = "Office"
  desktop_product_name_s = desktop_product_name.replace(" ", "")
  desktop_package_name = company_name + "-" + desktop_product_name_s
  desktop_changes_dir = "desktop-apps/win-linux/package/windows/update/changes"

if utils.is_macos():
  desktop_package_name = "TypsastraOffice"
  desktop_build_dir = "desktop-apps/macos"
  desktop_branding_dir = "desktop-apps/macos"
  desktop_updates_dir = "build/update"
  desktop_changes_dir = "TypsastraOffice/update/updates/TypsastraOffice/changes"
  sparkle_base_url = "https://github.com/Typsastra-Office/DesktopEditors/releases/download/appcast"

builder_product_name = "Document Builder"

if utils.is_linux():
  desktop_make_targets = [
    {
      "make": "tar",
      "src": "tar/*.tar*",
      "dst": "desktop/linux/generic/"
    },
    {
      "make": "deb",
      "src": "deb/*.deb",
      "dst": "desktop/linux/debian/"
    },
    {
      "make": "rpm",
      "src": "rpm/build/RPMS/*/*.rpm",
      "dst": "desktop/linux/rhel/"
    },
    {
      "make": "rpm-suse",
      "src": "rpm-suse/build/RPMS/*/*.rpm",
      "dst": "desktop/linux/suse/"
    }
  ]
  server_make_targets = [
    {
      "make": "deb",
      "src": "deb/*.deb",
      "dst": "server/linux/debian/"
    },
    {
      "make": "rpm",
      "src": "rpm/builddir/RPMS/*/*.rpm",
      "dst": "server/linux/rhel/"
    },
    {
      "make": "tar",
      "src": "*.tar*",
      "dst": "server/linux/snap/"
    }
  ]
