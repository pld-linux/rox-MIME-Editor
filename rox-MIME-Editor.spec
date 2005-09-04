%define _name MIME-Editor
Summary:	Graphical editor for MIME types
Summary(pl):	Graficzny edytor typów MIME
Name:		rox-%{_name}
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/mime-editor-%{version}.tgz
# Source0-md5:	957096e26d374233bb6954fcac2816ca
Source1:	%{name}.desktop
URL:		http://rox.sourceforge.net/phpwiki/index.php/MIME-Editor
Requires:	python-pygtk-gtk
Requires:	rox >= 2.3
Requires:	rox-Lib2 >= 1.9.7
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_roxdir	%{_libdir}/rox

%description
rox-MIME-Editor is a graphical editor for Shared MIME Database.

%description -l pl
rox-MIME-Editor jest graficznym edytorem dla dzielonej biblioteki MIME.

%prep
%setup -q -n mime-editor-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_roxdir}/%{_name}/{Help,Messages}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cd %{_name}
install .DirIcon App* *.py $RPM_BUILD_ROOT%{_roxdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Help
install Messages/*.gmo $RPM_BUILD_ROOT%{_roxdir}/%{_name}/Messages
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_comp $RPM_BUILD_ROOT%{_roxdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_roxdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_name}/Help/Changes
%attr(755,root,root) %{_roxdir}/%{_name}/AppRun
%dir %{_roxdir}/%{_name}
%{_roxdir}/%{_name}/Help
%{_roxdir}/%{_name}/.DirIcon
%{_roxdir}/%{_name}/*.xml
%{_roxdir}/%{_name}/*.py[co]
%dir %{_roxdir}/%{_name}/Messages
%lang(fr) %{_roxdir}/%{_name}/Messages/fr.gmo
%lang(it) %{_roxdir}/%{_name}/Messages/it.gmo
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
