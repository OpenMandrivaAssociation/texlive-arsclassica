# revision 23434
# category Package
# catalog-ctan /macros/latex/contrib/arsclassica
# catalog-date 2011-06-30 10:42:48 +0200
# catalog-license lppl
# catalog-version 2.7
Name:		texlive-arsclassica
Version:	2.7
Release:	1
Summary:	A different view of the ClassicThesis package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arsclassica
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arsclassica.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arsclassica.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package changes some typographical points of the
ClassicThesis style, by Andre Miede. It allows to reproduce the
look of the guide The art of writing with LaTeX (the web page
is in Italian).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/arsclassica/classic.ist
%{_texmfdistdir}/tex/latex/arsclassica/arsclassica.sty
%doc %{_texmfdistdir}/doc/latex/arsclassica/ArsClassica.pdf
%doc %{_texmfdistdir}/doc/latex/arsclassica/ArsClassica.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/Bibliography.bib
%doc %{_texmfdistdir}/doc/latex/arsclassica/CHANGES
%doc %{_texmfdistdir}/doc/latex/arsclassica/Chapters/Code.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/Chapters/Fundamentals.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Abstract+Sommario.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Acknowledgements.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Bibliography.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Contents.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Index.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Titleback.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Titlepage.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Birds.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_1.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_2.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_3.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_4.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/GuITlogo.pdf
%doc %{_texmfdistdir}/doc/latex/arsclassica/README
%doc %{_texmfdistdir}/doc/latex/arsclassica/arsclassica-preamble.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}
