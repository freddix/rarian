Summary:	Rarian is a documentation meta-data library
Name:		rarian
Version:	0.8.1
Release:	13
License:	LGPL v2+
Group:		Base
Source0:	http://ftp.gnome.org/pub/GNOME/sources/rarian/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	75091185e13da67a0ff4279de1757b94
URL:		http://rarian.freedesktop.org/
BuildRequires:	libxslt-devel
Requires:	coreutils
Requires:	gawk
Requires:	libxslt-progs
Requires:	util-linux
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rarian is a documentation meta-data library that allows access to
documents, man pages and info pages. It was designed as a replacement
for scrollkeeper.

%package libs
Summary:	Rarian library
License:	LGPL v2+
Group:		Libraries

%description libs
Rarian library.

%package devel
Summary:	Development files for Rarian
Group:		Development/Languages
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Developement files for rarian library.

%prep
%setup -q

%build
%configure \
	--enable-omf-read 	\
	--disable-skdb-update	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/omf

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/rarian-sk-update

%post	libs -p /usr/sbin/ldconfig
%postun libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING COPYING.LIB COPYING.UTILS ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/rarian-example
%attr(755,root,root) %{_bindir}/rarian-sk-*
%attr(755,root,root) %{_bindir}/scrollkeeper-*
%dir %{_datadir}/omf
%{_datadir}/librarian
%{_datadir}/help

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/librarian.so.?
%attr(755,root,root) %{_libdir}/librarian.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librarian.so
%{_libdir}/librarian.la
%{_includedir}/rarian
%{_pkgconfigdir}/rarian.pc

