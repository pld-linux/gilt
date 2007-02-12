Summary:	gilt - text oriented pictures editor
Summary(pl.UTF-8):   gilt - tekstowo zorientowany edytor obrazków
Name:		gilt
Version:	0.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://sol.spaceports.com/~engels/programming/unix/gilt/file/Gilt.java.final.tgz
# Source0-md5:	1a4c8400b2e90ed81381e0e5726a61d6
Patch0:		%{name}-configure.in.patch
URL:		http://sol.spaceports.com/~engels/programming/unix/gilt/
BuildRequires:	autoconf
BuildRequires:	automake
#Requires:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gilt is a text oriented picture editor.

%description -l pl.UTF-8
Gilt jest tekstowo zorientowanym edytorem obrazków.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
rm -rf config.*
%{__aclocal}
%{__autoconf}
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
