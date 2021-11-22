from views.mainView import MainView

def HomeView():
	
    html= """<div class="page-content">

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
											<img id="_stream" class="live-screen sc-screen"  alt="Loading..."/>
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
											<img id="cropped_stream" class="live-screen cr-screen"  alt="Loading..."/>
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
										<div class="card-body" style="padding-top:0">
											<div class="dashboard-social-list">
												<ul  class="list-group list-group-flush" id="lisence_plates">
													
													
													
												</ul>
											</div>
										</div>
									</div>
								</div>
								<div class="col-6 col-lg-6">
									<div class="card radius-15">
										<div class="card-header border-bottom-0">
											<div class="d-lg-flex align-items-center">
												<div>
													<h4 class="mb-lg-0">Whitelist Plate</h4>
												</div>

											</div>
										</div>
										<div class="card-body">
											<input type="text" id="lisence_plate"/>
											<button id="save_plate">Save</button>
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
										<img id="realtime_stream"  class="live-screen l-screen"  alt="Loading..."/>
									</div>
								</div>

							</div>
						</div>
					</div>
					<!--end row-->

		</div>"""
    return MainView(html)