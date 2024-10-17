Name:		texlive-ketcindy
Version:	58661
Release:	2
Summary:	macros for graphic generation and Cinderella plugin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ketcindy
License:	gpl3+
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ketcindy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ketcindy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
KETpic is a macro package designed for computer algebra systems
(CAS) to generate LaTeX source codes for high-quality
mathematical artwork. KETcindy is a plugin for Cinderella that
allows to generate graphics using KETpic. The generated code
can be included in any LaTeX document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist/tex/latex/ketcindy
%{_texmfdistdir}/texmf-dist/scripts/ketcindy
%doc %{_texmfdistdir}/texmf-dist/doc/support/ketcindy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
