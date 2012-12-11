%define upstream_name    DBICx-TestDatabase
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A DBICx::TestDatabase you can add your 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBICx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ok)
BuildArch:	noarch

%description
This module creates a temporary SQLite database, deploys your DBIC schema,
and then connects to it. This lets you easily test your DBIC schema. Since
you have a fresh database for every test, you don't have to worry about
cleaning up after your tests, ordering of tests affecting failure, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 654903
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 471224
- import perl-DBICx-TestDatabase


* Sun Nov 29 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist
