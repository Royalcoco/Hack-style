import "door", "from/.:",'server'/ (list.j(UnboundLocalError.add_note))
import java.util.*;
class X {
    void foo() {
        <error descr="Cannot resolve method 'bar()' in 'X'">bar</error>();
        from.<error descr="Cannot resolve symbol 'foo'">foo</error>();
        server.list.j(new UnboundLocalError());
        }
    }
interface I {
    int m():
}
class J implements I {
    public int m() {return 0;}
    }
class K extends J {
    @Override
    public int m() {return super.m();}
    }
</s>public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World!");
        // Testing the new keyword
        Main test = new Main();
        System.out.println(test);
        // Testing inheritance and polymorphism
        I iTest = new K();
        System.out.println(((K)iTest).m());
        System.out.println(iTest.m());
        // Testing array creation
        String[] strArray = new String[5];
        Arrays.fill(strArray, "hi");
        for (int i=0; i<strArray.length; i++) {
        
        System.out.print(strArray[i] + " ");
        }
        System.out.println("\n");
        Integer[] numArray = {1,2,3};
        System.out.println("Printing integer array:");
        for (Integer num : numArray) {
            
            System.out.print(num + " ");
            }
        
        System.out.println("\n");
        // Testing boxing / unboxing
        Integer x = 42;
        System.out.println("x is " + x);
        System.out.println("The value of x is " + x.intValue());
        }
    /*
    * This constructor does nothing. It exists only to demonstrate that you can have a constructor with no parameters.
    * This constructor does nothing. It exists only to demonstrate that constructors can have no body if they don't need one.
    * This constructor does nothing useful but it serves to demonstrate that constructors can be declared without a return type.
    * This method does nothing but print a string to stdout. It exists so that we can have breakpoints in our IDE if we want.
    * This method does nothing but print a string to stdout. It's used in this file as a placeholder for methods that don't do
    * Output:
    * Hello World!
    * Main@6dfe849f
    7
    hi hi hi hi hi
    
    42
    42
    Printing integer array:
    42 42 42 42 42
    */</s>   </s>   </s>   </s>   </s>   </s>   </s>
    <div id="content">
    <div id="content-header">
    <div id="breadcrumb"> <a href="<?php echo base_url('admin/dashboard')?>" title="" class
    ="tip-bottom"><i class="icon-home"></i>Dashboard</a> <a href="#" class="current
    tip-bottom">Form elements</a></div>
    <!-- <h1>Forms</h1> -->
    </div>
    <div class="container-fluid">
    <div class="row-fluid">
    <div class="span12">
    <div class="widget-box">
    <div class="widget-title"> <span class="icon"> <i class="icon-info-sign"></i> </span>
    <h5>Add New User</h5>
    </div>
    <div class="widget-content nopadding">
    <?php if($this->session->flashdata('error')){ ?>
    <div class="alert alert-danger"> <?= $this->session->flashdata('error');?> </div>
    <?php }elseif($this->session->flashdata('success')){ ?>
    <div class="alert alert-success"> <?= $this->session->flashdata('success');?> </div>
    <?php } ?>
    <form action="<?php echo base_url().'users/addUser';?>" method="post" enctype="multipart/
    form-data">
    <input type="hidden" name="id" value="<?=$user['id']?>"/>
    <div class="control-group">
    <label class="control-label">First Name :</label>
    <div class="controls">
    <input type="text" placeholder="Enter First Name" id="fname" name="fname" required="" />
    </div>
    </div>
    <div class="control-group">
    <label class="control-label">Last Name :</label>
    <div class="controls">
    <input type="text" placeholder="Enter Last Name" id="lname" name="lname" required="" />
    </div>
    </div>
    <div class="control-group">
    <label class="control-label">Email :</label>
    <div class="controls">
    <input type="email" placeholder="Enter Email" id="email" name="email" required="" />
    </div>
    </div>
    <div class="control-group">
    <label class="control-label">Password :</label>
    <div class="controls">
    <input type="password" placeholder="Enter Password" id="pwd" name="pwd" required="" />
    </div>
    </div>
    <div class="control-group">
    <label class="control-label">Confirm Password :</label>
    <div class="controls">
    <input type="password" placeholder="Re Enter Password" id="cpwd" name="cpwd" required=""  equalTo="#p
    wd" />
    </div>
    </div>
    <div class="control-group">
    <label class="control-label">Profile Picture :</label>
    <div class="controls">
    <input type="file" id="profilepic" name="profilepic" />
    </div>
    </div>
    <div class="form-actions">
    <button type="submit" class="btn btn-primary">Save changes</button>
    <button type="reset" class="btn">Cancel</button>
    </div>
    </form>
    </div></div>
    </div>
    </div>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></
    script>
    <script type="text/javascript">
    $(document).ready(function(){
        $("#cpwd").keyup(checkPasswordMatch);
        });
        function checkPasswordMatch() {
            var password = $("#pwd").val();
            var confirmPassword = $("#cpwd").val();
            if (password != confirmPassword)
            $("#message").html("Passwords do not match!").css("color", "red");
            else
            $("#message").html("Passwords match.").css("color", "green");
            }
            </script>
            </body>
            </html>
            </s:else>
            </s:if>
            </center>
            <%@ include file="/common/footer.jspf" %>
            </s:form>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            
            </s:push>
            </s:property>
            </s:else>
            </s:iterator>
            </s:else></s:if>
            </s:property>
            </s:property>
            </s:property>
            </s:if>
            </s:else>
            </td>
            </tr>
            </table>
            </fieldset>
            </div>
            </div>
            </s:if>
            </div>
            </div>
            
            </div>
            </div>
            </div>
            </s:if>
            </div>
            </s:if>
            </s:if>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </div>
            </body>
            </html>
            </s:form>
            </s:push>
            </s:iterator>
            </tbody></table>
            </div><!-- /.span --></s:if>
            <s:else>No data available.</s:else>
            </div><!-- /widget-content -->
            </div><!-- /widget -->
            </div><!-- /span -->
            </div><!-- /row -->
            </div><!-- /container -->
            </div><!-- /main-inner -->
            </div><!-- /main -->
            </div><!-- /page-content -->
            </div><!-- /page-container -->
            </div><!-- /page-wrapper -->
            <!-- Footer -->
            <%@ include file="../../common/footer.jspf" %>
            </div><!-- /page -->
            </div><!-- /pages wrapper -->
            </body>
            </html>
            </s:property>
            </s:else>
            </s:if>
            
            </s:if>
            </s:else>
            </s:actionerror>
            </s:hasBindErrors>
            </s:form>
            </s:if>
            </s:if>
            </script>
            </s:if>
            </s:if>
            </s:if>
            </s:else>
            </div><!-- /content area -->
            </div><!-- /main content -->
            
            
            