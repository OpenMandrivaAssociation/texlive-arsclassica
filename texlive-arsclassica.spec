Name:		texlive-arsclassica
Version:	45656
Release:	2
Summary:	A different view of the ClassicThesis package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/arsclassica
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arsclassica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arsclassica.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package changes some typographical points of the
ClassicThesis style, by Andre Miede. It enables the user to
reproduce the look of the guide The art of writing with LaTeX
(the web page is in Italian).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tlpkg/tlpobj/arsclassica*
%{_texmfdistdir}/tex/latex/arsclassica
%doc %{_texmfdistdir}/doc/latex/arsclassica

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tlpkg tex doc %{buildroot}%{_texmfdistdir}
