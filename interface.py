def MyHtml():
    PAGE = """\
  <!DOCTYPE html>
<html lang="en">

<head>
	<!-- Required meta tags -->
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
	<title>MSB Parking</title>
	<!--favicon-->
	<link rel="icon" href="/assets/images/favicon-32x32.png" type="image/png" />
	<!-- Vector CSS -->
	<link href="/assets/plugins/vectormap/jquery-jvectormap-2.0.2.css" rel="stylesheet" />
	<!--plugins-->
	<link href="/assets/plugins/simplebar/css/simplebar.css" rel="stylesheet" />
	<link href="/assets/plugins/perfect-scrollbar/css/perfect-scrollbar.css" rel="stylesheet" />
	<link href="/assets/plugins/metismenu/css/metisMenu.min.css" rel="stylesheet" />
	<!-- loader-->
	<link href="/assets/css/pace.min.css" rel="stylesheet" />
	<script src="/assets/js/pace.min.js"></script>
	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="/assets/css/bootstrap.min.css" />
	<!-- Icons CSS -->
	<link rel="stylesheet" href="/assets/css/icons.css" />
	<!-- App CSS -->
	<link rel="stylesheet" href="/assets/css/app.css" />


</head>

<body class="bg-theme bg-theme9">
	<!-- wrapper -->
	<div class="wrapper">
		<!--sidebar-wrapper-->
		<div class="sidebar-wrapper" data-simplebar="true">
			<div class="sidebar-header">
				<div class="">
					<img src="/assets/images/Logo.png" class="logo-icon-2" alt="" />
				</div>

				<a href="javascript:;" class="toggle-btn ml-auto"> <i class="bx bx-menu"></i>
				</a>
			</div>
			<!--navigation-->
			<ul class="metismenu" id="menu">

				<li class="menu-label">MENU</li>
				<li>
					<a href="index.html">
						<div class="parent-icon"><i class="bx bx-movie-play"></i>
						</div>
						<div class="menu-title">Live</div>
					</a>
				</li>
				<li>
					<a href="history.html">
						<div class="parent-icon"> <i class="bx bx-history"></i>
						</div>
						<div class="menu-title">History</div>
					</a>
				</li>
				<li>
					<a href="file-manager.html">
						<div class="parent-icon"><i class="bx bx-cog"></i>
						</div>
						<div class="menu-title">Settings</div>
					</a>
				</li>
				<li>
					<a href="contact-list.html">
						<div class="parent-icon"><i class="bx bx-server"></i>
						</div>
						<div class="menu-title">Api</div>
					</a>
				</li>


			</ul>
			<!--end navigation-->
		</div>
		<!--end sidebar-wrapper-->
		<!--header-->
		<header class="top-header">
			<nav class="navbar navbar-expand">
				<div class="left-topbar d-flex align-items-center">
					<a href="javascript:;" class="toggle-btn"> <i class="bx bx-menu"></i>
					</a>
				</div>
				<div class="flex-grow-1 search-bar">
					<div class="input-group">
						<div class="input-group-prepend search-arrow-back">
							<button class="btn btn-search-back" type="button"><i class="bx bx-arrow-back"></i>
							</button>
						</div>
						<h1>Live</h1>
					</div>
				</div>
				<div class="right-topbar ml-auto">
					<ul class="navbar-nav">
						<li class="nav-item search-btn-mobile">
							<a class="nav-link position-relative" href="javascript:;"> <i
									class="bx bx-search vertical-align-middle"></i>
							</a>
						</li>


						<li class="nav-item dropdown dropdown-user-profile">
							<a class="nav-link dropdown-toggle dropdown-toggle-nocaret" href="javascript:;"
								data-toggle="dropdown">
								<div class="media user-box align-items-center">
									<div class="media-body user-info">
										<p class="user-name mb-0">MSB</p>
										<p class="designattion mb-0">Parking</p>
									</div>
									<img src="/assets/images/logo_bg.png" class="user-img" alt="user avatar">
								</div>
							</a>

						</li>
						<li class="nav-item dropdown dropdown-language">
							<a class="nav-link dropdown-toggle dropdown-toggle-nocaret" href="javascript:;"
								data-toggle="dropdown">
								<div class="lang d-flex">
									<div>
										<i class="bx bx-log-out"></i>
									</div>
								</div>
							</a>

						</li>
					</ul>
				</div>
			</nav>
		</header>
		<!--end header-->
		<!--page-wrapper-->
		<div class="page-wrapper">
			<!--page-content-wrapper-->
			<div class="page-content-wrapper">
				<div class="page-content">

					<!--end row-->
					<div class="row">
						<div class="col-12 col-lg-5">
							<div class="row">
								
								<div class="col-12 col-lg-12">
									<div class="card radius-15">
										<div class="card-header border-bottom-0">
											<div class="d-lg-flex align-items-center">
												<div>
													<h4 class="mb-lg-0">Real Time</h4>
												</div>

											</div>
										</div>
										<div class="card-body">
											<img class="live-screen sc-screen" src="/stream.mjpg" alt="Loading..."/>
										</div>
									</div>
								</div>
								<div class="col-6 col-lg-6">
									<div class="card radius-15">
										<div class="card-header border-bottom-0">
											<div class="d-lg-flex align-items-center">
												<div>
													<h4 class="mb-lg-0">Scan Plate</h4>
												</div>

											</div>
										</div>
										<div class="card-body">
											<img class="live-screen cr-screen" src="/cropped.mjpg" alt="Loading..."/>
										</div>
									</div>
								</div>
								<div class="col-6 col-lg-6">
									<div class="card radius-15">
										<div class="card-header border-bottom-0">
											<div class="d-lg-flex align-items-center">
												<div>
													<h4 class="mb-lg-0">Scaned Plate List</h4>
												</div>

											</div>
										</div>
										<div class="card-body">
											<div class="dashboard-social-list">
												<ul class="list-group list-group-flush">
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li><li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													<li class="list-group-item d-flex align-items-center bg-transparent">
														<p class="mb-0">YouTube</p>														
													</li>
													
												</ul>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col-12 col-lg-7">
							<div class="card radius-15">
								<div class="card-body">
									<div class="d-lg-flex align-items-center">
										<div>
											<h4 class="mb-4">Live Cam</h4>
										</div>
									</div>
									<div>
										<img  class="live-screen l-screen" src="/realtime.mjpg" alt="Loading..."/>
									</div>
								</div>

							</div>
						</div>
					</div>
					<!--end row-->

				</div>
			</div>
			<!--end page-content-wrapper-->
		</div>
		<!--end page-wrapper-->
		<!--start overlay-->
		<div class="overlay toggle-btn-mobile"></div>
		<!--end overlay-->
		<!--Start Back To Top Button--> <a href="javaScript:;" class="back-to-top"><i
				class='bx bxs-up-arrow-alt'></i></a>
		<!--End Back To Top Button-->
		<!--footer -->
		<div class="footer">
			<p class="mb-0">MSB MMC @2021 </p>
		</div>
		<!-- end footer -->
	</div>

	<!--end switcher-->
	<!-- JavaScript -->
	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
	<script src="/assets/js/jquery.min.js"></script>
	<script src="/assets/js/popper.min.js"></script>
	<script src="/assets/js/bootstrap.min.js"></script>
	<!--plugins-->
	<script src="/assets/plugins/simplebar/js/simplebar.min.js"></script>
	<script src="/assets/plugins/metismenu/js/metisMenu.min.js"></script>
	<script src="/assets/plugins/perfect-scrollbar/js/perfect-scrollbar.js"></script>
	<!-- Vector map JavaScript -->
	<script src="/assets/plugins/vectormap/jquery-jvectormap-2.0.2.min.js"></script>
	<script src="/assets/plugins/vectormap/jquery-jvectormap-world-mill-en.js"></script>
	<script src="/assets/plugins/apexcharts-bundle/js/apexcharts.min.js"></script>
	<script src="/assets/js/index.js"></script>
	<!-- App JS -->
	<script src="/assets/js/app.js"></script>
	<script>
		new PerfectScrollbar('.dashboard-social-list');
		new PerfectScrollbar('.dashboard-top-countries');
	</script>
</body>

</html>
    """
    return PAGE
