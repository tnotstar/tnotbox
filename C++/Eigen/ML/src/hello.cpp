
#include <iostream>
#include <Eigen/Dense>

int
main () {

	std::cout << "Hello, Eigen!" << std::endl;

	Eigen::MatrixXd m(2, 2);

	m(0, 0) = 3;
	m(0, 1) = 2.5;
	m(1, 0) = -1;
	m(1, 1) = m(0, 1) + m(1, 0);

	std::cout << m << std::endl;

	return 0;
}

// EOF
