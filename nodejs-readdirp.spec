%{?scl:%scl_package nodejs-readdirp}
%{!?scl:%global pkg_name %{name}}

%global npm_name readdirp
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-%{npm_name}
Version:	2.0.0
Release:	13%{?dist}
Summary:	Recursive version of fs.readdir with streaming api.
Url:		https://github.com/thlorenz/readdirp
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(nave)
BuildRequires:	npm(tap)
BuildRequires:	npm(through2)
%endif

%description
Recursive version of fs.readdir with streaming api.

%prep
%setup -q -n package

%nodejs_fixdep minimatch

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
(cd test && set -e; for t in ./*.js; do node $t; done)"
nave use 0.8 npm run test-main
nave use 0.10 npm run test-main
nave use 0.12 npm run test-main
nave use 2.4 npm run test-main
npm run test-main && npm run test-0.8 && npm run test-0.10 && npm run test-0.12 && npm run test-2.4
if [ -e $TRAVIS ]; then npm run test-all; else npm run test-main; fi
%endif

%files
%{nodejs_sitelib}/readdirp

%doc README.md
%license LICENSE

%changelog
* Tue May 03 2016 root - 2.0.0-13
- Rebuild

* Tue May 03 2016 root - 2.0.0-12
- Fix dependencies

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-11
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-10
- Rebuilt with updated metapackage

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-9
- Fix version of event-stream
- Fix version of tap-stream

* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-3
- Enable scl macros

* Thu Dec 17 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-2
- Fix dependencies

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- update to upstream release 0.4.0

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.3-1
- initial package
