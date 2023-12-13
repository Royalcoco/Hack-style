import control from s2clientprotocol
<control_pb2'
import sc2api_connection as conn
from .game_data import GameData, UnitTypeId
class BotAI(object):
"""The base class for implementing an AI bot.
This is the main entry point for writing a custom bot. To implement your own bot, subclass this and override the necessary methods. The bot will
Subclasses should override the on_* methods to implement their bot's behavior.
"""
def __init__(self, game_info=None, save_replay=False, want_rgb=False):
"""Creates a new BotAI instance.
Parameters:
    - game_info: An optional dictionary containing initial game information. This can be used if your bot wants to act immediately at the start of the game
    - game_info: The initial game state. If None, it will be retrieved when needed (slow).
    Use this if you are running against a custom map or protocol build.
    - save_replay: Whether to save a replay at the end of each game.
    - want_rgb: Whether to render RGB observations. This is slow, so unset want_rgb if your bot doesn't use
    them (default False)
    """
    self._conn = None
    self.game_info = game_info
    self.save_replay = save_replay
    self.want_rgb = want_rgb
    
    def _ensure_connected(func):
    def wrapper(self, *args, **kwargs):
    if not self._conn:
    assert self.game_info, "Must set game_info before calling %s" % func.__name__
    self._connect()
    return func(self, *args, **kwargs)
    wrapper.__doc__ = func.__doc__
    return wrapper
    @property
    def client(self):
    
    """:class:`sc2lib.sc2_mock.MockClient`: The underlying SC2 API client."""
    
    return self._conn.client
    @_ensure_connected
    def step(self, actions):
    """Advances the simulation by one frame with the given action.
    Parameters:
    - actions : list of :class:`Action` instances
    Returns:
    tuple containing:
    - obs : :class:`Observation` instance
    - reward : float
    - done : bool
    
    - info : dict
    """
    result = self._conn.step([a.to_proto() for a in actions])
    observation = GameData().from_observation(result.observation)
    reward = result.reward
    done = result.done
    info = {"debug": result.debug}
    return observation, reward, done, info</s>   </s>  </s>
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Bootstrap Admin Dashboard Template</title>
    <!-- Bootstrap CSS -->
    {!! Html::style('css/bootstrap.min.css') !!}
    <!-- bootstrap theme -->
    {!! Html::style('css/bootstrap-theme.css') !!}
    <!--external css-->
    <!-- font icon -->
    {!! Html::style('fonts/font-awesome-4.7.0/css/font-awesome.min.css
    ') !!}
    <!-- Custom styles -->
    {!! Html::style('css/style.css') !!}
    {!! Html::script('js/jquery-1.9.1.js') !!}
    
    </head>
    <body>
    <nav class="navbar navbar-inverse navbar-fixed-top " role="navigation">
    
    <div class="container-fluid">
    <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">

    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#sidebar-collapse">
    <!-- Collapsed Hamburger -->
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#app-navbar-collapse
    <span class="sr-only">Toggle Navigation</span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
    <span class="icon-bar"></span>
    </button>
    <!-- Branding Image -->
    @if (Auth::guest())
    <a class="navbar-brand" href="{{ url('/') }}"><img src="/images/logo.png" alt="" /></
    a>
    @else
    <a class="navbar-brand" href="{{ route('dashboard', ['id' => Auth::user()->id]) }}">
    <div style="display: inline; vertical-align: middle;">
    <img src="/uploads/avatars/{{ Auth::user()->avatar }}" height="35px" width="auto
    "/>&nbsp;&nbsp;
    {{ Auth::user()->name }}
    </div>
    </a>
    @endif

    
    </div>
    <nav id="top-menu" class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <!-- Main Menu -->
    <div id="sidebar-collapse" class="collapse navbar-collapse">
    <ul class="nav metismenu" id="main-menu">
    @role(['admin','super_admin'])
    <li><!-- Dashboard -->
    <a href="javascript:void(0);" class="show-submenu">
    <i class="fa fa-dashboard"></i>&nbsp;Dashboard</a>
    <ul class="nav collapse">
    <li><a href="{{ route('dashboard', ['id' => Auth::user()->id]) }}">Overview</a></
    li>
    <li><a href="{{ route('users.index') }}">Users Management</a></li>
    </ul>
    </li>
    @endrole
    @can('create post')
    <li><!-- Blog -->
    <a href="{{ route('posts.create') }}"><i class="fa fa-pencil"></i>&nbsp;New Post</
    a></li>
    @endcan
    <li><!-- Posts -->
    
    <a href="{{ route('posts.index') }}"><i class="fa fa-file-text-o"></i>&nbsp;
    
    Posts</a></li>
    <li><!-- Categories -->
    <a href="{{ route('categories.index') }}"><i class="fa fa-list"></i>&nbsp;Categories</
    
    a></li>
    <li><!-- Comments -->
    
    <a href="#"><i class="fa fa-comment"></i>&nbsp;Comments<span class="pull-right label label-
    <?php
    
    $total = DB::table('comments')->count();
    if ($total > 0 && $total <= 2) {
        echo 'warning';
        } elseif($total > 2){
            echo 'danger';
            }else{
                
                echo 'success';
                
                }
                ?>">{{$total}}</span></a></li>
                <li><!-- Settings -->
                <a href="javascript:void(0)" class="show-submenu">
                <i class="fa fa-cog"></i>&nbsp;Settings</a>
                <ul class="nav nav-second-level collapse">
                <li><a href="{{route('profile.edit',['username'=>Auth::user()->username])}}">Profile</a></li
                >
                <li><a href="{{ route('settings') }}">General</a></li></ul></li>
                <!--   @include('partials._notifications') -->
                </ul>
                </div>
                </div>
                </div>
                @stop
                @section('content')
                
                <div id="page-wrapper" style="min-height: 579px;">
                @yield('post-content')
                
                
                
                </div>
                @stop
                @section('footer')
                
                <div id="footer">
                <div class="container text-center">
                <p>Copyright &copy; {{ date("Y") }} <a href="/">Laravel Blog</a>. Theme by
                <a href="http://startbootstrap.com/template-overviews/sb-admin-2">SB Admin 2</a>,
                
                designed and customized by <a href="https://github.com/jbrooksuk">James Brookes</a>.</p
                </div>
                
                
                </div>
                @stop
                @section('scripts')
                <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.js"></
                script>
                <script type="text/javascript" src="{{ asset('/assets/js/metisMenu.js')
                }}"></script>
                <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"><
                /script>
                <script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.
                js"></script>
                <script src="{{asset ('assets/js/morris.js')}}"></script>
                
                <script src="//cdn.ckeditor.com/4.4.6/standard/ckeditor.js"></script>
                <script>CKEDITOR.replace('body');</script>
                
                <script src="{{ asset('/assets/js/custom.js') }}"></script>
                <script>
                $(document).ready(function() {
                    $('#side-menu').metisMenu();
                    });
                    </script>
                    @if (Session::has('success'))
                    <script>
                    swal({title: "Success!", text: "{{ Session::get('success') }}", type: "success"}, function(){
                        swal({title:"Success!",text:"{{ Session::get('success') }}",type:"success"},
                            function(){location.reload();});
                        </script>
                        
                        @endif
                        @if ($errors->any())
                        
                        
                        <script>swal({title:"Error!",text:"Please check the form for errors.",type: "error"});</script
                        <!--   Only show error notification if there is an actual error to display -->
                        <script>swal({title: "Error!",text: "@foreach($errors->all() as $error)<li>
                                    {{ $error }}</li>@endforeach",type: "error"});</script>
                        @endif
                        </script>
                        </html>
                        </div></s>
                        #include "stdafx.h"
                        
                        #include "CppUnitTest.h"
                        using namespace Microsoft::VisualStudio::CppUnitTestFramework;
                        TEST_CLASS(MyTests)
                        {
                            public:
                                /*
                                * Testing the addition of two integers
                                */
                                TEST_METHOD(AdditionOfTwoIntegers)
                                {
                                    int a = 5, b = 8;
                                    Assert::AreEqual(13, a + b);
                                    }
                                };
                        </s>
                        #include "gtest/gtest.h"
                        #include "../src/utilities/StringManipulation.hpp"
                        // The fixture for testing class Foo.
                        
                        class StringManipulationTest : public ::testing::Test
                        }
                        protected:
                             // If the constructor and destructor are not enough for setting up
                             // and tearing down each test, you can define the following methods:
                                virtual void SetUp()
                                {
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test)
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // Code here will be called immediately after the constructor (right before each test).
                                     // _ensure_connected
                                    }
                                virtual void TearDown()
                                {
                                     // _disconnect
                                    }
                                };
                    /**
                    * @brief Checks if string is empty or not
                    */
                    TEST_F(StringManipulationTest, IsEmpty)
                    {
                        std::string str("");
                        ASSERT_TRUE(is_empty(str));
                        }
                    /**
                    * @brief Checks if string is not empty
                    */
                    
                    TEST_F (StringManipulationTest, NotIsEmpty)
                    {
                        std::string str("Hello World!");
                        ASSERT_FALSE(is_empty(str));
                        }
                    /**
                    * @brief Appends two strings
                    */
                    TEST_F(StringManipulationTest, AppendStrings)
                    
                    
                    {
                        std::string s1 = "Hello";
                        std::string s2 = "World!";
                        append_strings(s1, s2);
                        ASSERT_EQ(s1, "HelloWorld!");
                        s1 = "1234567890";
                        append_strings(s1, s2);.Bring.sum(self, *args, **kwargs):
                                return super().bring
                                .sum(*args, **kwargs) + len(self._name)</s>
                                #include <stdio.h>
                                #include "gtest/gtest.h"
                                class MyTestFixture : public ::testing::Test {
                                    
                                    protected:
                                        MyTestFixture() {}
                                        ~MyTestFixture() {}
                                        
                                        void SetUp() override {
                                            printf("SetUp\n");
                                            }
                                        void TearDown() override {
                                            printf("TearDown\n");
                                            }
                                        };
                                // Test Fixture for testing add function
                                
                                TEST_F(MyTestFixture, AddFunction) {
                                    int a = 1;
                                    int b = 2;
                                    
                                    EXPECT_EQ(a+b, 3);
                                    }</s>}</s>}
                    }
                    } else {
                        /* No match found in the table - use default action */
                        rv = BCMFP_FILTER_SELECTOR_ERROR;
                        }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    }
                    
                    }
                    
                    
                    }
                    }
                    if (BCMFP_ACTIONS_ATTRS_CHECK(unit)) {
                        
                        /* Check that all attributes are set correctly. */
                        rv = bcmfp_actions_attrs_check(unit, stage,
                                                    &grp_oper->action_res_id,
                                                    &grp_oper->action_res_chunk_id,
                                                    grp_oper->num_actions,
                                                    fg->flags);
                        }
                    }
                    }
                    }
                    }
                    }
                    break;
                case BCMFP_GROUP_MODE_PORT:
                    case BCMFP_GROUP_MODE_LPORT:
                        case BCMFP_GROUP_MODE_HPORT:
                            key_size = 0;
                            data_size = 0;
                            num_qos_prof = 0;
                            
                            num_ltpr_prof = 1;
                            num_tcAMs = 1;
                            num_packet_format_types = 1;
                            num_vlan_format_types = 1;
                            num_ip_protocol_types = 1;

                            
                            num_tcp_ctl_bits = 8;
                            num_udp_ctl_bits = 8;
                            num_icmp_type_groups = 4;
                            num_mpls_specs = 3;
                            num_vxlan_vpn = 2;
                            is_presel = FALSE;
                            id_alloc_one = TRUE;
                            action_res_id_valid = TRUE;
                            action_res_level = BCMFP_HA_BLK_ENTRY_ID;
                            blk_id = -1;
                            chunk_id = -1;
                            