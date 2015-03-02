Summary:	The Table engine for IBus platform
Summary(pl.UTF-8):	Silnik Table dla platformy IBus
Name:		ibus-table
Version:	1.5.0
Release:	2
License:	LGPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus/downloads/list
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	6f46912e52bf683fa1177787507205f5
Patch0:		ibus-table-uppercase-umlauts.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	ibus-devel > 1.4.99
BuildRequires:	python >= 1:2.5
Requires:	ibus > 1.4.99
Requires:	%{name}-engine = %{version}-%{release}
Requires:	ibus >= 1.3.0
Requires:	python-dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Table engine for IBus platform.

%description -l pl.UTF-8
Silnik Table dla platformy IBus.

%package engine
Summary:	IBus Table engine
Summary(pl.UTF-8):	Silnik IBus Table
Group:		Applications/Text
Requires:	python-modules >= 1:2.5
Requires:	python-modules-sqlite >= 1:2.5

%description engine
IBus Table engine.

%description engine -l pl.UTF-8
Silnik IBus Table.

%package devel
Summary:	Development files for ibus-table
Summary(pl.UTF-8):	Pliki programistyczne dla ibus-table
Group:		Development/Tools
Requires:	%{name}-engine = %{version}-%{release}

%description devel
Development files for ibus-table.

%description devel -l pl.UTF-8
Pliki programistyczne dla ibus-table.

%prep
%setup -q
%patch0 -p1

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-table
%{_datadir}/ibus/component/table.xml
%{_datadir}/%{name}/engine/factory.py
%{_datadir}/%{name}/engine/factory.pyc
%{_datadir}/%{name}/engine/factory.pyo
%{_datadir}/%{name}/engine/main.py
%{_datadir}/%{name}/engine/main.pyc
%{_datadir}/%{name}/engine/main.pyo
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

%files engine -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/pinyin_table.txt.bz2
%dir %{_datadir}/%{name}/engine
%{_datadir}/%{name}/engine/tabcreatedb.py
%{_datadir}/%{name}/engine/tabcreatedb.pyc
%{_datadir}/%{name}/engine/tabcreatedb.pyo
%{_datadir}/%{name}/engine/tabdict.py
%{_datadir}/%{name}/engine/tabdict.pyc
%{_datadir}/%{name}/engine/tabdict.pyo
%{_datadir}/%{name}/engine/table.py
%{_datadir}/%{name}/engine/table.pyc
%{_datadir}/%{name}/engine/table.pyo
%{_datadir}/%{name}/engine/tabsqlitedb.py
%{_datadir}/%{name}/engine/tabsqlitedb.pyc
%{_datadir}/%{name}/engine/tabsqlitedb.pyo
%dir %{_datadir}/%{name}/tables
%{_datadir}/%{name}/tables/template.txt

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-createdb
%{_pkgconfigdir}/%{name}.pc
