TEMPLATE = subdirs

SUBDIRS += \
    tide \
    roothelper

OTHER_FILES += \
    rpm/harbour-tide-editor.spec \
    harbour-tide-editor.desktop

desktop.files =  harbour-tide-editor.desktop
desktop.path =  /usr/share/applications/

INSTALLS += desktop
