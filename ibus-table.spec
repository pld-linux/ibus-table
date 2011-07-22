Summary:	The Table engine for IBus platform
Name:		ibus-table
Version:	1.3.0.20100621
Release:	0.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0fd5812197400f7b586480fca1a0c082
URL:		http://code.google.com/p/ibus/
BuildRequires:	ibus-devel > 1.3.0
Requires:	ibus > 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Table engine for IBus platform.

%package devel
Summary:	Development files for ibus-table
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development files for ibus-table.

%prep
%setup -q

%build
%configure \
	--disable-additional

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/%{name}-createdb
%attr(755,root,root) %{_libexecdir}/ibus-engine-table
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/engine
%dir %{_datadir}/%{name}/tables
%dir %{_datadir}/%{name}/icons
%dir %{_datadir}/%{name}/data
%{_datadir}/ibus/component/table.xml
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
%{_datadir}/%{name}/data/pinyin_table.txt.bz2
%{_datadir}/%{name}/engine/factory.py
%{_datadir}/%{name}/engine/factory.pyc
%{_datadir}/%{name}/engine/factory.pyo
%{_datadir}/%{name}/engine/main.py
%{_datadir}/%{name}/engine/main.pyc
%{_datadir}/%{name}/engine/main.pyo
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
%{_datadir}/%{name}/tables/template.txt

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/%{name}.pc
