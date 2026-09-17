#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Typsastra branding entry point.
#
# Invoked by the workspace build_tools/make.py with OO_RUNNING_BRANDING=1 and
# cwd = <workspace>/typsastra/build_tools. It sets brand-specific build
# variables and then hands over to the workspace make.py (which skips the
# branding block because OO_RUNNING_BRANDING is inherited).

import os
import subprocess
import sys

BRAND_COMPANY = "Typsastra"
BRAND_PRODUCT = "Typsastra Office"
BRAND_SITE = "https://github.com/Typsastra-Office"
BRAND_SUPPORT = "https://github.com/Typsastra-Office/DesktopEditors/issues"
BRAND_RELEASES = "https://github.com/Typsastra-Office/DesktopEditors/releases"
BRAND_COPYRIGHT = "Copyright (C) Typsastra. Based on ONLYOFFICE, Copyright (C) Ascensio System SIA."


def set_env(name, value):
    os.environ[name] = value


def main():
    # Windows updmodule update channels
    set_env("DESKTOP_URL_UPDATES_MAIN_CHANNEL", BRAND_RELEASES + "/latest/download/appcast.json")
    set_env("DESKTOP_URL_UPDATES_DEV_CHANNEL", BRAND_RELEASES + "/download/appcastdev/appcastdev.json")

    # web-apps help entry point
    set_env("DESKTOP_URL_WEBAPPS_HELP", BRAND_SITE)

    # core qmake version resources (QMAKE_TARGET_COMPANY/COPYRIGHT)
    set_env("PUBLISHER_NAME", BRAND_COMPANY)
    set_env("COPYRIGHT_OWNER", "Based on ONLYOFFICE, (c) Ascensio System SIA. Modified by Typsastra 2026.")

    # web-apps / sdkjs build identity (Gruntfile placeholder replacements)
    set_env("APP_COPYRIGHT", BRAND_COPYRIGHT)
    set_env("PUBLISHER_NAME", BRAND_COMPANY)
    set_env("PUBLISHER_URL", BRAND_SITE)
    set_env("COMPANY_NAME", BRAND_PRODUCT)
    set_env("APP_TITLE_TEXT", BRAND_PRODUCT)
    set_env("HELP_URL", BRAND_SITE)
    set_env("SUPPORT_URL", BRAND_SUPPORT)
    set_env("SUGGEST_URL", BRAND_SUPPORT)
    set_env("SUPPORT_EMAIL", "")
    set_env("SALES_EMAIL", "")

    workspace_build_tools = os.path.abspath(
        os.path.dirname(os.path.abspath(__file__)) + "/../../build_tools"
    )
    # subprocess instead of os.execv: on Windows execv spawns a new process and
    # exits the caller, which breaks every wait() up the call chain
    ret = subprocess.call(
        [sys.executable, "make.py"] + sys.argv[1:], cwd=workspace_build_tools
    )
    sys.exit(ret)


if __name__ == "__main__":
    main()
