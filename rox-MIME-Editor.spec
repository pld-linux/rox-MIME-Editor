%define _name MIME-Editor
Summary:	Graphical editor for MIME types
Summary(pl):	Graficzny edytor typów MIME
Name:		rox-%{_name}
Version:	0.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/mime-editor-%{version}.tgz
# Source0-md5:	9ccf56f0188ce59225f2acf49b0bf02d
Source1:	%{name}.desktop
URL:		http://rox.sourceforge.net/phpwiki/index.php/MIME-Editor
Requires:	python-pygtk-gtk
Requires:	rox-Lib2
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
rox-MIME-Editor is a graphical editor for Shared MIME Database.

%description -l pl
rox-MIME-Editor jest graficznym edytorem dla dzielonej biblioteki MIME.

%prep
%setup -q -n mime-editor-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,Messages}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cd %{_name}
install .DirIcon App* *.py $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install Messages/*.gmo $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Messages
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/Changes
%attr(755,root,root) %dir %{_appsdir}
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%dir %{_appsdir}/%{_name}
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/*.py[co]
%dir %{_appsdir}/%{_name}/Messages
%lang(it) %{_appsdir}/%{_name}/Messages/it.gmo
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
