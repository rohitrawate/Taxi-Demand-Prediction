<?php
session_start();
//error_reporting(0);
include('includes/config.php');
if (strlen($_SESSION['uid']==0)) {
  header('location:logout.php');
  } else{
   
?>
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Customer Purchase Prediction</title>

    <!-- Custom fonts for this template-->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="css/sb-admin-2.min.css" rel="stylesheet">

</head>

<body id="page-top">

    <!-- Page Wrapper -->
    <div id="wrapper">

        <!-- Sidebar -->
       <?php include_once('includes/sidebar.php');?>
        <!-- End of Sidebar -->

        <!-- Content Wrapper -->
        <div id="content-wrapper" class="d-flex flex-column">

            <!-- Main Content -->
            <div id="content">

                <!-- Topbar -->

                    <!-- Topbar Navbar -->
  <?php include_once('includes/topbar.php');?>
                <!-- End of Topbar -->

                <!-- Begin Page Content -->
                <div class="container-fluid">

                    <!-- Page Heading -->
                    <div class="d-sm-flex align-items-center justify-content-between mb-4">
 <h1 class="h3 mb-0 text-gray-800"><?php echo ucwords($_SESSION['fname']);?>'s Profile</h1>
                    </div>

                    <div class="row">
<form method="post" action="processac.php">
	
		Text:<br>
		<input type="text" name="bal">
		<br>
Text:<br>
		<input type="text" name="bal">
		<br>
Text:<br>
		<input type="text" name="bal">
		<br>
Text:<br>
		<input type="text" name="bal">
		<br>
Text:<br>
		<input type="text" name="bal">
		<br>
		<input type="submit" name="save" value="submit">
	</form>
                        <div class="col-lg-12">

<?php 
$uid=$_SESSION['uid'];
 $query = "SELECT * FROM `predict`;";
  
  // FETCHING DATA FROM DATABASE
  $result = $con->query($query);


while ($row = $result->fetch_assoc()) {

?>


                            <!-- Default Card Example -->
                            <div class="card mb-4">
                                <div class="card-header">
                                 Prediction
                                </div>
                                <div class="card-body">
					
             <table class="table table-bordered dataTable" id="dataTable" width="100%" cellspacing="0" role="grid" aria-describedby="dataTable_info" style="width: 100%;">
                                 
                 
                                        
                                    <tr>
                                            <th>Sr.No</th>
                                            <th>Cluster</th>
											<th>month</th>
<th>day</th>
<th>hour</th>
<th>dayofweek</th>
<th>count</th>
											
                                        </tr>
                                        <tr>
                                           <td><?php echo $row['id'];?></td>
                                            <td><?php echo $row['a'];?></td>
  <td><?php echo $row['b'];?></td>
  <td><?php echo $row['c'];?></td>
  <td><?php echo $row['d'];?></td>
  <td><?php echo $row['e'];?></td>
											<td><?php echo $row['presult'];?></td>
                                        </tr>
                                        
                                </table>
                                </div>
                            </div>
<?php } ?>

                        </div>

                    </div>

                </div>
                <!-- /.container-fluid -->

            </div>
            <!-- End of Main Content -->

            <!-- Footer -->
     <?php include_once('includes/footer.php');?>
            <!-- End of Footer -->

        </div>
        <!-- End of Content Wrapper -->

    </div>
    <!-- End of Page Wrapper -->

    <!-- Scroll to Top Button-->
    <a class="scroll-to-top rounded" href="#page-top">
        <i class="fas fa-angle-up"></i>
    </a>

    <!-- Logout Modal-->
     <?php include_once('includes/logout-modal.php');?>
    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>
</body>
</html>
<?php } ?>