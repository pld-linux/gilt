Summary:	gilt
Summary(pl):	gilt
Name:		gilt
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	%{name}.tgz
Patch0:		%{name}-configure.in.patch
#BuildRequires:	
#Requires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description

%description -l pl

%prep
%setup -q -n %{name}
%patch -p0

%build
rm -rf config.*
aclocal
autoconf
#CPPFLAGS="%{rpmcflags} -Wall -Iusr/X11R6 -I%{_includedir}" \
#CPP="%{__cc} %{rpmcflags} -Wall -Iusr/X11R6 -I%{_includedir}" \
#INCLUDEDIR="-I%{_includedir}" \
CFLAGS="-I%{_includedir} "	\
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
#%attr(,,)
