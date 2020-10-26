Name:           mysqlpump
Version:        1.0
Release:        1%{?dist}
Summary:        -

License:        -
URL:            -

BuildRequires: cmake3 openssl-devel ncurses-devel readline-devel libcurl-devel bison boost

Source0: 	patch

%description

%setup -q

%build
ldconfig -p | grep boost_regex
ln -s /lib64/libboost_regex.so.1.53.0 /lib64/libboost_regex.so
git clone https://github.com/percona/percona-server.git
cd percona-server/
git checkout 5.7
git submodule init && git submodule update
patch client/dump/table.cc %SOURCE0
mkdir build && cd build
cmake ../ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=/opt/ -DENABLE_DOWNLOADS=1 -DCMAKE_CXX_LINK_FLAGS=-lboost_regex
cd client
make -j8 && make install

%install
mkdir -p %{buildroot}/usr/bin
cp -R /usr/local/mysql/bin/mysqlpump %{buildroot}/usr/bin/tsum-mysqlpump

%files
/usr/bin/tsum-mysqlpump

%doc

%changelog