from views.mainView import MainView
from  database import selectCars

def WhitelistView():
    result=""
    i=0
    for row in selectCars():
        result+="<tr><td>"+str(i)+"</td><td>"+str(row[1])+"</td><td>"+str(row[2])+"</td><td></td></tr>"
        i+=1

    PAGE="""<div class="page-wrapper">
			<div class="page-content">
				
				<h6 class="mb-0 text-uppercase">White List</h6>
                
				<hr/>
				<div class="card">
					<div class="card-body">
						<div class="table-responsive">
							<table id="example" class="table table-striped table-bordered" style="width:100%">
								<thead>
									<tr>
										<th>#</th>
										<th>Lisence Plate</th>
										<th>Date</th>
										<th>-</th>
										
									</tr>
								</thead>
								<tbody>
									"""+result+"""
								</tbody>
								
							</table>
						</div>
					</div>
				</div>
				
			</div>
		</div>"""
    
    return MainView(PAGE)