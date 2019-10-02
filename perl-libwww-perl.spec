# 
# Do not Edit! Generated by:
# spectacle version 0.18
# 
# >> macros
# << macros

Name:       perl-libwww-perl
Summary:    A Perl interface to the World-Wide Web
Version:    5.837
Release:    2
Group:      Development/Libraries
License:    GPL+ or Artistic
BuildArch:  noarch
URL:        http://search.cpan.org/dist/libwww-perl/
Source0:    http://www.cpan.org/authors/id/G/GA/GAAS/libwww-perl-%{version}.tar.gz
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:   perl(Compress::Zlib)
Requires:   perl-HTML-Parser >= 3.33
BuildRequires:  perl(HTML::Entities), perl(URI), perl(Test::More), perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Compress::Zlib)


%description
The libwww-perl collection is a set of Perl modules which provides a
simple and consistent application programming interface to the
World-Wide Web.  The main focus of the library is to provide classes
and functions that allow you to write WWW clients. The library also
contain modules that are of more general use and even classes that
help you implement simple HTTP servers.



# Remove not-packaged features
%filter_from_requires /perl(Authen::NTLM)/d
%filter_from_requires /perl(HTTP::GHTTP)/d
%filter_from_requires /perl(Win32)/d
# Remove underspecified dependencies
%filter_from_requires /^perl(Encode)\s*$/d
%filter_from_requires /^perl(File::Listing)\s*$/d
%filter_from_requires /^perl(HTTP::Date)\s*$/d
%filter_from_requires /^perl(HTTP::Negotiate)\s*$/d
%filter_from_requires /^perl(HTTP::Request)\s*$/d
%filter_from_requires /^perl(HTTP::Response)\s*$/d
%filter_from_requires /^perl(HTTP::Status)\s*$/d
%filter_from_requires /^perl(LWP::MediaTypes)\s*$/d
%filter_from_requires /^perl(MIME::Base64)\s*$/d
%filter_from_requires /^perl(Net::HTTP)\s*$/d
%filter_from_requires /^perl(URI)\s*$/d
%filter_from_requires /^perl(WWW::RobotRules)\s*$/d
%filter_setup


%prep
%setup -q -n libwww-perl-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

if test -f Makefile.PL; then
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?jobs:-j%jobs}
else
%{__perl} Build.PL  --installdirs vendor
./Build
fi

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre

# Use system wide MIME types (link also to blib/... for "make test").  Doing
# << install pre
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs vendor
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

# >> install post
chmod -R u+w $RPM_BUILD_ROOT/*
for file in $RPM_BUILD_ROOT%{_mandir}/man3/LWP.3pm AUTHORS README Changes; do
iconv -f iso-8859-1 -t utf-8 < "$file" > "${file}_"
mv -f "${file}_" "$file"
done
# but a copy of /etc/mime.types.
for file in {blib/lib,$RPM_BUILD_ROOT%{perl_vendorlib}}/LWP/media.types ; do
[ ! -f $file ] && echo ERROR && exit 1
ln -sf /etc/mime.types $file
done

# << install post
%check
# >> check
#Disable test as we know we can't mail on the builder
#make test
# << check






%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS Changes README*
%{_bindir}/*
%{perl_vendorlib}/lwp*.pod
%{perl_vendorlib}/LWP.pm
%{perl_vendorlib}/Bundle/
%{perl_vendorlib}/File/
%{perl_vendorlib}/HTML/
%{perl_vendorlib}/HTTP/
%{perl_vendorlib}/LWP/
%{perl_vendorlib}/Net/
%{perl_vendorlib}/WWW/
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3*
# << files


