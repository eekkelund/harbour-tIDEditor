Name:       harbour-tide-editor

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    transportable IDE - editor
Version:    0.2.10
Release:    1
Group:      Qt/Qt
License:    GPLv3
URL:        https://github.com/eekkelund/harbour-tIDEditor
Source0:    %{name}-%{version}.tar.bz2
Requires:   sailfishsilica-qt5 >= 0.10.9, pyotherside-qml-plugin-python3-qt5 >= 1.3
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
transportable Editor for SailfishOS devices. Just the editor part of tIDE

%prep
%setup -q -n %{name}-%{version}


%build

%qtc_qmake5  \
    VERSION=%{version} \
    NAME=%{name}

%qtc_make %{?_smp_mflags}


%install
rm -rf %{buildroot}

%qmake5_install

%files
%exclude %{_datadir}/%{name}/qml/pages/BuildOutput.qml
%exclude %{_datadir}/%{name}/qml/template-app
%exclude %{_datadir}/%{name}/qml/pages/CreateProject.qml
%exclude %{_datadir}/%{name}/qml/pages/ProjectHome.qml
%exclude %{_datadir}/%{name}/qml/pages/AppOutput.qml
%exclude %{_datadir}/%{name}/qml/python/createProject.py
%exclude %{_datadir}/%{name}/qml/python/stopProject.py
%exclude %{_datadir}/%{name}/qml/python/buildRPM.py
%exclude %{_datadir}/%{name}/qml/python/deleteProject.py
%defattr(-,root,root,-)
%{_bindir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#%%defattr(4755,root,root,4755)
#%%{_bindir}/harbour-tide-editor-root
