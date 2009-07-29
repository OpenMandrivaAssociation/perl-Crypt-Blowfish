%define upstream_name	 Crypt-Blowfish
%define upstream_version 2.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl Blowfish encryption module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:	 perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module to encrypt using the Blowfish algorithm.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYRIGHT Changes
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/*/*
