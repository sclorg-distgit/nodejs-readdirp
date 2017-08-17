%{?scl:%scl_package nodejs-readdirp}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}
%global enable_tests 0

Name:       %{?scl_prefix}nodejs-readdirp
Version:    2.1.0
Release:    3%{?dist}
Summary:    Recursive version of Node's fs.readdir with a streaming API
License:    MIT
URL:        https://github.com/thlorenz/readdirp
Source0:    http://registry.npmjs.org/readdirp/-/readdirp-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(tap)
BuildRequires:  %{?scl_prefix}npm(through2)
%endif

%description
%{summary}.

%prep
%setup -q -n package

%nodejs_fixdep minimatch

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/readdirp
cp -pr package.json readdirp.js stream-api.js \
    %{buildroot}%{nodejs_sitelib}/readdirp

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
%__tap test/*.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md examples/
%license LICENSE
%{nodejs_sitelib}/readdirp

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.0-3
- rh-nodejs8 rebuild

* Tue Nov 01 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.0-2
- Remove useless fixdeps

* Mon Oct 31 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.0-1
- Updated with script

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
