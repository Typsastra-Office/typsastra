# Typsastra branding overrides for desktop-apps/package/Makefile.
# Included via -include $(BRANDING_DIR)/branding.mk after the defaults are
# evaluated, so derived variables are set explicitly.

COMPANY_NAME = Typsastra
PRODUCT_NAME = Office
PRODUCT_NAME_SHORT = Office
COMPANY_NAME_LOW = typsastra
PRODUCT_NAME_LOW = office

PACKAGE_NAME = typsastra-office
PACKAGE_OPENSOURCE = typsastra-office
PACKAGE_COMMERCIAL = typsastra-office-enterprise

PUBLISHER_NAME = Typsastra
PUBLISHER_URL = https://github.com/Typsastra-Office
SUPPORT_URL = https://github.com/Typsastra-Office/DesktopEditors/issues
SUPPORT_MAIL = 

SCHEME_HANDLER = typsastra-office

# desktop-apps/package/Makefile computes these with := at lines 62, 63 and 89,
# before this file is included, so they keep the ONLYOFFICE defaults and the
# Linux packages would look for build_tools/out/linux_64/onlyoffice and install
# under /opt/onlyoffice. Restate them recursively so they resolve after the
# branding above.
DESKTOPEDITORS_PREFIX = $(COMPANY_NAME_LOW)/$(PRODUCT_NAME_LOW)
DESKTOPEDITORS_EXEC = $(PACKAGE_NAME)
SOURCE_DIR = ../../build_tools/out/$(PLATFORM)/$(COMPANY_NAME_LOW)
