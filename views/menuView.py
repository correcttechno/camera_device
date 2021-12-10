def MenuView():
    return """<!--sidebar-wrapper-->
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
					<a class="has-arrow" href="javascript:;" >
						<div class="parent-icon"> <i class="bx bx-list-ul"></i>
						</div>
						<div class="menu-title">White List</div>
					</a>
					<ul>
						<li> <a href="whitelist.html"><i class="bx bx-list-ol"></i>List</a>
						</li>
						<li> <a href="whitelistadd.html"><i class="bx bx-add-to-queue"></i>Add</a>
						</li>
						
					</ul>
				</li>
				<li>
					<a href="file-manager.html">
						<div class="parent-icon"><i class="bx bx-cog"></i>
						</div>
						<div class="menu-title">Settings</div>
					</a>
				</li>
				<li>
					<a href="api.html">
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
		<!--end header-->"""