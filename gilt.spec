Summary:	gilt
Summary(pl):	gilt
Name:		gilt
Version:	0.0.2
Release:	1
Copyright:	GPL
Group:		graphics
Group(pl):	grafika
Source:		%{name}.tgz
Patch:		gilt-configure.in.patch
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
 
%description -l pl

%prep
%setup -q -n %{name}

%patch -p0

%build
rm -rf config.*
aclocal
autoconf
#CPPFLAGS="$RPM_OPT_FLAGS -Wall  -Iusr/X11R6 -I/usr/X11R6/include"	\
#CPP="gcc $RPM_OPT_FLAGS -Wall -Iusr/X11R6 -I/usr/X11R6/include"	\
#INCLUDEDIR="-I/usr/X11R6/include" \
CFLAGS="-I/usr/include "	\
./configure --prefix=%{_prefix}
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
