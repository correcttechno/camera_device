from views.mainView import MainSimpleView, MainView


def LoginView():
    PAGE="""
    <div class="wrapper">
		<div class="section-authentication-login align-items-center justify-content-center">
			<div class="row">
				<div class="col-12 col-lg-8 mx-auto">
					<div class="card radius-15">
						<div class="row no-gutters">
							<div class="col-lg-7">
								<div class="card-body p-md-5">
									<div class="text-center">
										<h3 class="mt-4 font-weight-bold">Welcome</h3>
									</div>
									
									<div class="form-group mt-4">
										<label>Username</label>
										<input id="username" type="text" class="form-control"
											placeholder="Enter your email username" />
									</div>
									<div class="form-group">
										<label>Password</label>
										<input id="password" type="password" class="form-control" placeholder="Enter your password" />
									</div>
									<div id="msg"></div>
									<div class="btn-group mt-3 w-100">
										
										<button id="login_btn" type="button" class="btn btn-light btn-block">
                                            Log In
										</button>
									</div>
									
								</div>
							</div>
							<div class="col-lg-5">
								<img width="100" height="100" src="/assets/images/Logo.png" class="card-img login-img h-100"
									alt="...">
							</div>
						</div>
						<!--end row-->
					</div>
				</div>
			</div>
		</div>
	</div>
    
    """
    return MainSimpleView(PAGE)