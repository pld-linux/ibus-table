Summary:	The Table engine for IBus platform
Summary(pl.UTF-8):	Silnik Table dla platformy IBus
Name:		ibus-table
Version:	1.17.8
Release:	1
# parts LGPL v2.1+, LGPL v3.0+, GPL v2+ => the result is GPL v3+
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/kaio/ibus-table/releases
Source0:	https://github.com/kaio/ibus-table/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	082dd6e75297442e03c6e728ae226d95
URL:		https://github.com/kaio/ibus-table
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	ibus-devel > 1.5.0
BuildRequires:	python3 >= 1:3.6
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sed >= 4.0
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name}-engine = %{version}-%{release}
Requires:	ibus >= 1.5.0
Requires:	python3-ibus >= 1.5.0
Requires:	python3-modules >= 1:3.6
Requires:	python3-pygobject3 >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binaries; not noarch because of ibus module dir
%define		_enable_debug_packages	0

%define		_libexecdir	%{_libdir}/ibus

%description
The Table engine for IBus platform.

%description -l pl.UTF-8
Silnik Table dla platformy IBus.

%package engine
Summary:	IBus Table engine
Summary(pl.UTF-8):	Silnik IBus Table
License:	LGPL v3+
Group:		Applications/Text
Requires:	python3-modules >= 1:3.6

%description engine
IBus Table engine.

%description engine -l pl.UTF-8
Silnik IBus Table.

%package devel
Summary:	Development files for ibus-table
Summary(pl.UTF-8):	Pliki programistyczne dla ibus-table
License:	LGPL v3+
Group:		Development/Tools
Requires:	%{name}-engine = %{version}-%{release}

%description devel
Development files for ibus-table.

%description devel -l pl.UTF-8
Pliki programistyczne dla ibus-table.

%prep
%setup -q

# one python version is enough
%{__sed} -i -e '1s,/usr/bin/python$,%{__python3},' engine/chinese_variants.py

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{pt_PT,pt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/ibus-setup-table
%attr(755,root,root) %{_libexecdir}/ibus-engine-table
%{_datadir}/%{name}/data/coin9.wav
%{_datadir}/%{name}/engine/factory.py
%{_datadir}/%{name}/engine/it_*.py
%{_datadir}/%{name}/engine/main.py
%{_datadir}/%{name}/engine/table.py
%{_datadir}/%{name}/engine/version.py
%{_datadir}/%{name}/engine/__pycache__/factory.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/it_*.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/main.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/table.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/version.cpython-*.py[co]
%{_datadir}/%{name}/icons
%{_datadir}/%{name}/setup
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
%{_datadir}/ibus/component/table.xml
%{_datadir}/metainfo/ibus-table.appdata.xml
%{_desktopdir}/ibus-setup-table.desktop
%{_iconsdir}/hicolor/*x*/apps/ibus-table.png
%{_iconsdir}/hicolor/scalable/apps/ibus-table.svg

%files engine -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/phrase.txt.bz2
%{_datadir}/%{name}/data/pinyin_table.txt.bz2
%dir %{_datadir}/%{name}/engine
%{_datadir}/%{name}/engine/chinese_variants.py
%{_datadir}/%{name}/engine/ibus_table_location.py
%{_datadir}/%{name}/engine/tabcreatedb.py
%{_datadir}/%{name}/engine/tabsqlitedb.py
%dir %{_datadir}/%{name}/engine/__pycache__
%{_datadir}/%{name}/engine/__pycache__/chinese_variants.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/ibus_table_location.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/tabcreatedb.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/tabsqlitedb.cpython-*.py[co]
%dir %{_datadir}/%{name}/tables
%{_datadir}/%{name}/tables/template.txt

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ibus-table-createdb
%{_pkgconfigdir}/ibus-table.pc
%{_mandir}/man1/ibus-table-createdb.1*
