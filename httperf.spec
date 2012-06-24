Summary:	httperf - a tool for measuring web server performance
Summary(pl):	httperf - narz�dzie do mierzenia wydajno�ci serwera HTTP
Name:		httperf
Version:	0.8
Release:	2
License:	GPL
Group:		Applications/Networking
URL:		http://www.hpl.hp.com/research/linux/httperf/
Source0:	ftp://ftp.hpl.hp.com/pub/httperf/%{name}-%{version}.tar.gz
# Source0-md5:  2971956d4846349f9e8d3c54acd591a5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel
Requires:	openssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Httperf is a tool for measuring web server performance. It provides a
flexible facility for generating various HTTP workloads and for
measuring server performance. The focus of httperf is not on
implementing one particular benchmark but on providing a robust,
high-performance tool that facilitates the construction of both micro-
and macro-level benchmarks. The three distinguishing characteristics
of httperf are its robustness, which includes the ability to generate
and sustain server overload, support for the HTTP/1.1 and SSL
protocols, and its extensibility to new workload generators and
performance measurements.

%description -l pl
Httperf jest narz�dziem mierz�cym wydajno�� serwera HTTP. Daje
elastyczne mo�liwo�ci generowania r�nego rodzaju obci��enia HTTP i
mierzenia wydajno�ci serwera. Httperf nie skupia si� na implementacji
jednego konkretnego testu wydajno�ci, ale na zapewnieniu pot�nego,
wysoko wydajnego narz�dzia u�atwiaj�cego tworzenie test�w wydajno�ci w
skali mikro i makro. Trzy cechy wyr�niaj�ce httperf to moc, daj�ca
mo�liwo�� generowania i podtrzymywania obci��enia serwera, obs�uga
protoko��w HTTP/1.1 i SSL oraz rozszerzalno�� o nowe generatory i
mierniki wydajno�ci.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install httperf $RPM_BUILD_ROOT%{_bindir}
install httperf.man $RPM_BUILD_ROOT%{_mandir}/man1/httperf.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO NEWS ChangeLog
%attr(755,root,root) %{_bindir}/httperf
%{_mandir}/man1/httperf.1*
