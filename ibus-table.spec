Summary:	The Table engine for IBus platform
Summary(pl.UTF-8):	Silnik Table dla platformy IBus
Name:		ibus-table
Version:	1.9.25
Release:	1
# parts LGPL v2.1+, LGPL v3.0+, GPL v2+ => the result is GPL v3+
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/kaio/ibus-table/releases
Source0:	https://github.com/kaio/ibus-table/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5f885b715a374d479574af53999e9864
URL:		https://github.com/kaio/ibus-table
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	ibus-devel > 1.5.0
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sed >= 4.0
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name}-engine = %{version}-%{release}
Requires:	ibus >= 1.5.0
Requires:	python3-ibus >= 1.5.0
Requires:	python3-modules >= 1:3.3
Requires:	python3-pygobject3 >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	python3-modules >= 1:3.3

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
%{_datadir}/%{name}/engine/factory.py
%{_datadir}/%{name}/engine/it_util.py
%{_datadir}/%{name}/engine/main.py
%{_datadir}/%{name}/engine/table.py
%{_datadir}/%{name}/engine/__pycache__/factory.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/it_util.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/main.cpython-*.py[co]
%{_datadir}/%{name}/engine/__pycache__/table.cpython-*.py[co]
%dir %{_datadir}/%{name}/icons
%{_datadir}/%{name}/icons/%{name}.svg
%{_datadir}/%{name}/icons/full-letter.svg
%{_datadir}/%{name}/icons/full-punct.svg
%{_datadir}/%{name}/icons/half-letter.svg
%{_datadir}/%{name}/icons/half-punct.svg
%{_datadir}/%{name}/icons/onechar.svg
%{_datadir}/%{name}/icons/phrase.svg
%{_datadir}/%{name}/icons/py-mode.svg
%{_datadir}/%{name}/icons/tab-mode.svg
%{_datadir}/%{name}/icons/chinese.svg
%{_datadir}/%{name}/icons/acommit.svg
%{_datadir}/%{name}/icons/english.svg
%{_datadir}/%{name}/icons/ncommit.svg
%{_datadir}/%{name}/icons/cb-mode.svg
%{_datadir}/%{name}/icons/sc-mode.svg
%{_datadir}/%{name}/icons/scb-mode.svg
%{_datadir}/%{name}/icons/tc-mode.svg
%{_datadir}/%{name}/icons/tcb-mode.svg
%dir %{_datadir}/%{name}/setup
%{_datadir}/%{name}/setup/*.py
%{_datadir}/%{name}/setup/*.ui
%{_datadir}/%{name}/setup/__pycache__
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
%{_datadir}/ibus/component/table.xml
%{_datadir}/metainfo/ibus-table.appdata.xml
%{_desktopdir}/ibus-setup-table.desktop

%files engine -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
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
