%define _unpackaged_files_terminate_build 1

%define modulename browsr
%def_with check

Name: python3-module-%modulename
Version: 1.21.0
Release: alt1

Summary: A pleasant file explorer in your terminal supporting all filesystems
License: MIT
Group: Other
Url: https://juftin.com/browsr/
Vcs: https://github.com/juftin/browsr.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pyperclip
BuildRequires: python3-module-click
BuildRequires: python3-module-textual_universal_directorytree
BuildRequires: python3-module-rich-click
%endif

%description
browsr is a pleasant file explorer in your terminal. It's a command
line TUI (text-based user interface) application that empowers you
to browse the contents of local and remote filesystems with your
keyboard or mouse.

%prep
%setup

%build
#export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
#Disable network tests and without modules
%pyproject_run_pytest -ra tests \
    --ignore tests/test_browsr.py \
    --ignore tests/test_cli.py \
    --ignore tests/test_config.py \
    -ra tests -k " \
    not test_github_screenshot and \
    not test_github_screenshot_license and \
    not test_mkdocs_screenshot"

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
#%doc README.md LICENSE docs/contributing.md docs/index.md docs/cli.md