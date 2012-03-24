/*
------- [ momentum jQuery CMS plugin ] -------

version: 0.0.1
edited: 2/29/12

© momentum labs 2012

-------------- [ momentum.io ] ---------------
 */

(function($, window, document, undefined) {


var editing, style_cache, state, change_count, falses, features, templates, methods, _flatten, _is, panel, buttons;
  
editing = false;
style_cache = {};
state = {};
change_count = 0;

features = {
  panel: {
    commands: {
      undo: function() {
        return document.execCommand('undo');
      },
      redo: function() {
        return document.execCommand('redo');
      },
      cut: function() {
        return document.execCommand('cut');
      },
      paste: function() {
        return document.execCommand('paste');
      },
      table: function() {
        return document.execCommand('enableInlineTableEditing');
      },
      resize: function() {
        return document.execCommand('enableObjectResizing');
      },
      clip: null,
      b: function() {
        return document.execCommand('bold');
      },
      u: function() {
        return document.execCommand('underline');
      },
      i: function() {
        return document.execCommand('italic');
      },
      clear: function() {
        return document.execCommand('removeFormat');
      },
      h1: function() {
        var t;
        t = document.selection ? document.selection() : window.getSelection();
        return document.execCommand('insertHTML', false, '<h1 class="h1">' + String(t) + '</h1>');
      },
      h2: function() {
        var t;
        t = document.selection ? document.selection() : window.getSelection();
        return document.execCommand('insertHTML', false, '<h2 class="h2">' + String(t) + '</h2>');
      },
      h3: function() {
        var t;
        t = document.selection ? document.selection() : window.getSelection();
        return document.execCommand('insertHTML', false, '<h3 class="h3">' + String(t) + '</h3>');
      },
      fontColor: function() {
        var c;
        c = prompt('Please enter a hexidecimal color value (i.e. #ffffff)');
        return document.execCommand('foreColor', false, c);
      },
      fontSize: function() {
        var s,t;
        t = document.selection ? document.selection() : window.getSelection();
        s = prompt('Please enter a desired point size, (e.g. enter 10 for 10pt)');
        return document.execCommand('insertHTML', false, '<span style="font-size:'+s+'pt;">'+t+'</span>');
      },
      fontFace: null,
      l: function() {
        return document.execCommand('justifyLeft');
      },
      r: function() {
        return document.execCommand('justifyRight');
      },
      c: function() {
        return document.execCommand('justifyCenter');
      },
      in: function() {
        return document.execCommand('indent');
      },
      out: function() {
        return document.execCommand('outdent');
      },
      bullet: function() {
        return document.execCommand('insertUnorderedList');
      },
      number: function() {
        return document.execCommand('insertOrderedList');
      },
      indentSpecial: null,
      lineSpacing: null,
      link: function() {
        var l;
        l = prompt('What URL would you like to link to?');
        return document.execCommand('createLink', false, l);
      },
      image: null,
      video: null
    },
    html: ['<div id="CMS_wrap">', '<div id="CMS_panel" class="fixed panel" style="opacity: 0;">', '<div id="CMS_frame" class="nowrap">', '<div class="cms_pane" id="buttons">', '<div class="cms_subpane">', '<h1 class="cms_sp">editing</h1>', '<p>', '<button id="cms_undo" value="undo">undo</button>', '<button id="cms_redo" value="redo">redo</button>', '<button id="cms_cut" value="cut">cut</button>', '<button id="cms_paste" value="paste">paste</button>', '</p>', '</div>', '<hr/>', '<div class="cms_subpane">', '<h1 class="cms_sp">typography</h1>', '<p>', '<select id="cms_headers" class="cms">', '<option id="cms_h1" class="h1">Heading 1</option>', '<option id="cms_h2" class="h2">Heading 2</option>', '<option id="cms_h3" class="h3">Heading 3</option>', '</select>', '<button id="cms_b" value="bold">B</button>', '<button id="cms_u" value="underline">U</button>', '<button id="cms_i" value="italic">I</button>', '<button id="cms_clear" value="clear formatting">clear</button>', '<button id="cms_fontColor" value="font color">font color</button>', '<button id="cms_fontSize" value="font size">font size</button>', '</p>', '</div>', '<hr/>', '<div class="cms_subpane">', '<h1 class="cms_sp">alignment</h1>', '<p style="text-lign:center">', '<button id="cms_l" value="left">left</button>', '<button id="cms_c" value="center">center</button>', '<button id="cms_r" value="right">right</button>', '<br>', '<button id="cms_in" value="indent">&raquo;</button>', '<button id="cms_out" value="outdent">&laquo;</button>', '<br>', '<button id="cms_ul" value="unordered list">&lt;ul&gt;</button>', '<button id="cms_ol" value="ordered list">&lt;ol&gt;</button>', '</p>', '</div>', '<hr/>', '<div class="cms_subpane">', '<h1 class="cms_sp">interactive</h1>', '<p>', '<button id="cms_link" value="link">add link</button>', '</p>', '</div>', '</div>', '<div class="cms_pane" id="styles">', '<div class="cms_subpane">', '<h1 class="cms_sp">styles</h1>', '<p>MIDDLE</p>', '</div>', '</div>', '<div class="cms_pane" id="assets">','<div class="cms_subpane">','<h1 class="cms_sp">assets</h1>','<div id="upload_wrap">','<div id="upload" class="dragdrop">','<span class="center-text" id="up_content">+</span>','</div>','</div>','</div>','<hr>','<div class="cms_subpane">','<h1 class="cms_sp">pop out</h1>','<p>','<button id="pop_assets_button" class="pop" name="assets" value="pop out this pane!">pop me out</button>','</p>','</div>','</div>','</div>', '<div id="CMS_nav">', '<a class="scroll" href="#buttons">buttons</a>', '<a class="scroll" href="#styles">styles</a>', '<a class="scroll" href="#assets">assets</a>', '</div>', '<div id="CMS_panel_footer">&copy; momentum labs 2012</div>', '</div>', '</div>'].join('\n')
  },
  scroller:
  {
    animation:
    {
      duration: 500,
      easing: 'easeInOutExpo',
      complete: null
    },

    axis: 'horizontal',
    frame: 'CMS_frame',
    init: false
  },
  pop:
  {
    position:
    {
      bottom: '60px',
      right: '60px'
    },

    animation:
    {
      duration: 500,
      easing: 'easeInOutExpo',
      complete: null
    },

    init: false
  },
  modal:
  {
    initial:
    {
      width: '0px',
      height: '0px',
      top: window.innerHeight/2 + 'px',
      left: window.innerWidth/2 + 'px'
    },

    ratio: {
      x: 0.4,
      y: 0.4
    },

    template: [
      '<div id="[% id %]_container" style="opacity: 0;" class="container">',
        '<div id="[% id %]" style="opacity: 0;" class="modal">',
          '<div id="[% id %]_status"></div>',
          '<hr>',
          '<div id="[% id %]_content">',
          '</div>',
          '<hr>',
          '<div id="[% id %]_ui"></div>',
        '</div>',
      '</div>'
    ].join('\n'),

    rounded: true,
    init: false
  },

  overlay: '<div id="m-overlay" class="fixed" style="opacity: 0;"></div>',
  init: false,
};

methods = {

  init : function(cfg) {

    config = $.extend(true, {}, features, cfg);

    $('body').append('<div class="fixed panel bigger" id="cms_edit_on" style="vertical-align: middle; left: -305px;top: 10px;width: 300px;text-align: right;padding-right: 10px;opacity: 0;"><span id="cms_span" style="opacity:0;">content editing <span style="color: green;font-weight: bold;">ON</span></span></div>');
    setTimeout(function() {
      $('#cms_span').animate({'opacity':1},{duration: 450,easing: 'easeInOutExpo'});
      $('#cms_edit_on').animate({
        'opacity': 1,
        'left': '-155px'
      }, {
        duration: 400,
        easing: 'easeInOutExpo',
        complete: function() {
          setTimeout(function() {
            $('#cms_span').animate({
              'opacity': 0
            }, {
              duration: 350,
              easing: 'easeInOutExpo'
            });
            $('#cms_edit_on').animate({
              'left': '-290px'
            }, {
              duration: 500,
              easing: 'easeInOutExpo',
              complete: function() {
                $('#cms_edit_on').html('&raquo;');
                $('#cms_edit_on').css({'cursor': 'pointer'});
                util.bind($('#cms_edit_on'), 'click', function(){
                  panel.make();
                  panel.live();
                  $('#cms_edit_on').html('X');
                  $('#cms_edit_on').unbind('click');
                  util.bind($('#cms_edit_on'), 'click', util.wrap(panel.destroy, true));
                });
              }
            });
          }, 1750);
        }
      });
    }, 500);

    return this.each(function() {
      var t = this, $t = $(t);

      util.bind($t, 'click', util.wrap(methods.edit, t));
    });

  },

  edit : function(o) {

    var $o = $(o),
      offset = $o.offset(),
      $id = $o.attr('id');

    style_cache[$id] = $o.attr('style');
    state[$id] = $o.html();

    o.contentEditable = true;
    editing = true;

    $o.unbind('click');

    over = config.overlay;

    $('body').append(over);
    $('#m-overlay').animate({
      'opacity': 0.75
    }, {
      duration: 400,
      easing: 'easeInOutExpo'
    });

    // bring element forward & disable page
    $o.css({
      'z-index': function() {
        var z = 900 + Math.floor(Math.random() * 81);
        return z;
      },
      'position': 'absolute'
    });
    $o.offset(offset);

    if (!util.isID('CMS_panel'))
    {
      panel.make();
      panel.live();
    }

    $('#m-overlay').bind({
      click: util.wrap(methods.save, o)
    });


  },

  save : function(ob) {

    var $o = $(ob),
      $id = $o.attr('id'),
      inHTML = $o.html(),
      $kn = $o.data('snippet-keyname') ? $o.data('snippet-keyname') : 'default-key';


    console.log('RETRIEVING HTML STATE: '+state[$id]+'COMPARED TO: '+inHTML);

    editing = false;
    ob.contentEditable = false;

    panel.destroy();

    console.log('REBINDING EDIT ON '+$o);

    util.bind($o, 'click', util.wrap(methods.edit, ob));

    if (!util.isID('CMS_sync'))
    {
      $('body').append('<div class="cms_message warn" id="CMS_sync" style="opacity: 0;"><div id="sync_loader" class="loader">syncing changes...</div></div>')
    }

    $('#m-overlay').animate({
      'opacity': 0
    }, {
      duration: 500,
      easing: 'easeInOutExpo',
      complete: function() {
        $('#m-overlay').remove();
        if (inHTML !== state[$id])
        {
          $('#CMS_sync').animate({
            'opacity': 1
          }, {
            duration: 700,
            easing: 'easeInOutExpo',
            complete: function() {
                change_count++;
                methods.sync({
                  snippet_keyname: $kn,
                  inner_html: inHTML
                });
              }
          });
        }
      }
    });
  },

  sync : function(snippetObj) { 

    console.log('SYNC!')
    console.log('Change Count: '+change_count);

    $.apptools.api.content.save_snippet(snippetObj).fulfill(
    {
      success : function() {
        if (change_count-1 == 0)
        {
          $('#CMS_sync').html('changes saved!');
          $('#CMS_sync').removeClass('warn').removeClass('error').addClass('yay');
          setTimeout(function() {
            $('#CMS_sync').animate({
              'opacity': 0
            }, {
              duration: 500,
              easing: 'easeInOutExpo',
              complete: function() {
                $('#CMS_sync').remove();
              }
            });
          }, 700);
          change_count--;
        }
        else {
          change_count--;
        }
      },
      failure : function(error) {
        $('#CMS_sync').html('error syncing page.');
        $('#CMS_sync').removeClass('warn').addClass('error');
        setTimeout(function() {
          $('#CMS_sync').append('<br><a id="sync_retry" style="pointer: cursor;text-decoration: underline;">retry sync</a>');
          util.bind($('#sync_retry'), 'click', util.wrap(methods.sync, snippetObj));
        }, 1500);
      }
    });
  },

  revert : function(oBj) {

    var _o = obj,
      keyn = $(obj).data('snippet-keyname');

    if (util.is(keyn))
    {
      $.apptools.api.content.revert_snippet({snippet_keyname: keyn}).fulfill(
      {
        failure : function() {
          //
        },

        success : function(response) {
          $(_o).html(response.inner_html);
          $('body').append('<div id="CMS_revert" class="cms_message yay" style="opacity: 0;">changes reverted!</div>');
          $('#CMS_revert').animate({'opacity': 1}, {
            duration: 400,
            easing: 'easeInOutExpo',
            complete: function() {
              setTimeout(function() {
                $('#CMS_revert').animate({'opacity': 0}, {
                  duration: 500,
                  easing: 'easeInOutExpo',
                  complete: function() {
                    $('#CMS_revert').remove();
                  }
                });
              });
            }
          });
        }
      });
    }
  },

  refresh : function() {

    // Refresh content item

  },

  uploadAsset : function(ev) {
    ev.preventDefault();
    ev.stopPropagation();

    console.log('File(s) dropped!')
    $(ev.target).removeClass('hover');

    var fi;

    fi = ev.dataTransfer.files;

    for (var i = 0; i < fi.length; i++)
    {
      var file = fi[i],
        imgType = /image.*/;

        console.log('WORKING ON FILE '+file.name)

        if (!file.type.match(imgType))
        {
          continue;
        }

      console.log('FILE TYPE: '+file.type);
      document.getElementById('upload').innerHTML = '';

      var reader = new FileReader();
      reader.onloadend = util.imgPreview;
      reader.readAsDataURL(file);
      
    }

    // $.apptools.api.upload.generate_upload_url
  },

  placeAsset : function() {

  }

};

util = {

  bind : function(obj, ev, fnc) {

    var rObj = {};
    rObj[ev] = fnc;

    return obj.bind(rObj);
  },

  imgPreview : function(eV) {

    var res = eV.target.result,
      img = document.createElement('img');

    img.classList.add('preview');
    img.src = res;

    document.getElementById('upload').appendChild(img);
    console.log('RESULTS ARE IN: '+res);

  },

  is : function(thing) {

    if ($.inArray(thing, [false, null, NaN, undefined, 0, {}, [], '','false', 'False', 'null', 'NaN', 'undefined', '0', 'none', 'None']) === -1)
    {
      return true;
    }
    else
    {
      return false;
    }
  },

  isID : function(str) {

    if (String(str).split('')[0] === '#' || document.getElementById(str) !== null)
    {
      return true;
    }
    else
    {
      return false;
    }
  },

  makeDragDrop : function(elem) {

    elem.addEventListener('dragenter', util.stopEvent, false);
    elem.addEventListener('dragexit', util.stopEvent, false);
    elem.addEventListener('dragleave', util.stopEvent, false);
    elem.addEventListener('dragover', util.stopEvent, false);
    elem.addEventListener('drop', methods.uploadAsset, false);
  },

  stopEvent : function(e) {

    e.preventDefault();
    e.stopPropagation();

    et = e.target;

    if (e.type === 'dragenter')
    {
      console.log('event triggered: '+e.type);
      $(et).addClass('hover');
    }
    else if (e.type !== 'dragover')
    {
      console.log('event triggered: '+e.type);
      $(et).removeClass('hover');
    }
  },

  wrap : function(func) {

    var args = Array.prototype.slice.call(arguments, 1);

    return function() {
      func.apply(this, args);
    };
  }
};

panel = {

  make : function() {
    var raw = config.panel.html;
    
    // create & animate control panel
    $('body').append(raw);
    $('#CMS_panel').css({
      'bottom': '0px'
    });

    $('#CMS_wrap').css({'opacity': 1});
    $('#CMS_panel').animate(
    {
      'bottom': '60px',
      'opacity': 1
    }, {
      'duration': 500,
      'easing': 'easeInOutExpo'
    });
  },

  live : function() {
    var cmds = config.panel.commands,
      up = document.getElementById('upload');

    // init scrollable content
    console.log('Enabling scrollable content...');
    $('.scroll').each(function() {
      var t, $t, rel;

      t = this;
      $t = $(t);
      rel = String($t.attr('href')).slice(1);

      $t.attr('id', 'scr-'+rel);
      $t.attr('href','javascript:void(0);');

      $t.data('scroller', {
        target: rel,
        frame: config.scroller.frame
      });
      $('#'+config.scroller.frame).data('scroller', {axis: 'horizontal'});

      util.bind($t, 'click', util.wrap(scroller.jump, rel));
    });
    config = $.extend(true, {}, config, {scroller: {init: true}});
    scroller.classify(config.scroller.frame);

    // init popouts
    console.log('Packaging pop-out content...');
    $('.pop').each(function() {
      var t, $t, rel;

      t = this;
      $t = $(t);
      rel = $t.attr('name')

      $t.removeAttr('name');

      $t.data('pop', {
        target: rel
      });

      util.bind($t, 'click', util.wrap(pop.pop, rel));
    });

    config = $.extend(true, {}, config, {pop: {init: true}});

    // init upload drag & drop

    util.makeDragDrop(up);

    console.log('BINDING PANEL ACTIONS')
    for (var bu in cmds)
    {
      axn = cmds[bu];
      if (axn !== null)
      {
        $('#cms_'+bu).bind({
          click: axn
        });
      }
    }
  },

  die: function() {
    var _cmds = config.panel.commands;

    console.log('UNBINDING PANEL ACTIONS');

    for (var _bu in _cmds)
    {
      _axn = _cmds[_bu];
      if (_axn !== null)
      {
        $('#cms_'+_bu).unbind('click');
      }
    }
  },

  destroy : function(deep) {

    deep = true;

    $('#m-overlay').unbind();

    if (editing === false)
    {
      $('#CMS_panel').animate(
      {
        'opacity': 0,
        'bottom': '0px'
      }, {
        duration: 450,
        easing: 'easeInOutExpo',
        complete: function() {
          if (deep === true)
          {
            $('#CMS_wrap').remove();
          }
          else
          {
            $('#CMS_wrap').css({
              'opacity': 0
            });
          }
        }
      });
    }
  }
};

scroller = {

  classify : function(ctx) {

    var $c = $('#'+ctx),
      $d = $c.data('scroller');

    if ($d.axis === 'horizontal' || ! util.is($d.axis))
    {
      console.log('Horizontal scroll detected. Adjusting classes...');
      $('.cms_pane').removeClass('left').removeClass('clear').addClass('in-table');
      $c.addClass('nowrap');
    }
    else if ($d.axis === 'vertical')
    {
      console.log('Vertical scroll detected. Adjusting classes...');
      $c.removeClass('nowrap');
      $('.cms_pane').removeClass('in-table').addClass('left').addClass('clear');
    }
  },

  jump : function(reL, cback, e) {

    if (util.is(e))
    {
      e.preventDefault();
      e.stopPropagation();
    }
    var t_o, r_o,
      $f = $('#'+config.scroller.frame),
      $d = $f.data('scroller'),
      anim = util.is(cback) ?
        $.extend({}.config.scroller.animation, {complete: cback}) :
        config.scroller.animation;


    console.log('Scrolling to #'+reL);

    f_o = $f.offset(),
    r_o = $('#'+reL).offset();

    if ($d.axis === 'vertical')
    {
      diff = Math.floor(r_o.top - f_o.top);

      $f.animate({
        scrollTop: '+='+diff
      }, anim);
    }

    else if ($d.axis === 'horizontal')
    {
      diff = Math.floor(r_o.left - f_o.left);

      $f.animate({
        scrollLeft: '+='+diff
      }, anim);
    }
  }
};

pop = {

  pop: function(iD, conf) {
    var $b, $t, _anim, biD, pHTML, piD, popped, pos, prevSib;

    pos = config.pop.position;

    $t = $('#'+iD);
    piD = 'pop_'+iD;
    biD = piD+'_button';
    $b = $('#'+biD);

    pHTML = $t.html();
    prevSib = $t.prev().attr('id');

    $b.unbind('click');
    _anim = $.extend({}, config.pop.animation, {
      complete: function() {
        $t.remove();
        $('#'+biD).html('pop back in');
        util.bind($('#'+biD), 'click', util.wrap(pop.reset, iD, 'CMS_frame'));
      }
    });

    console.log('OHHHHHHHHHHHH SNAP ITS _ANIM: '+_anim.complete);

    console.log('POPPING #'+iD+' OUT TO #'+piD+' AND REBINDING #'+biD);

    popped = '<div id="'+piD+'" class="fixed panel" style="opacity: 0;">'+pHTML+'</div>';
    $('body').append(popped);

    $('#'+piD).css({
      'bottom': '0px',
      'right': pos.right,
      'z-index': 989
    });
    $('#'+piD).animate({
      'bottom': pos.bottom,
      'opacity': 1
    }, _anim);

    scroller.jump(prevSib);
  },

  reset : function(id, tid) {

    if (tid === false || !util.is(tid))
    {
      $('#pop_'+id).remove();
    }
    else
    {
      var $t, _anim, bid, pid, phtml, ppane;

      pid = 'pop_'+id;
      $t = $('#'+tid);
      bid = pid+'_button';

      $(bid).unbind('click');
      _anim = $.extend({}, config.pop.animation, {
        complete: function() {
          $('#'+pid).remove();
          $('#'+bid).html('pop back in');
          util.bind($('#'+bid), 'click', util.wrap(pop.pop, id, 'CMS_frame'));
        }
      });

      phtml = $('#'+pid).html();
      ppane = '<div class="cms_pane" id="'+id+'">'+phtml+'</div>';

      $t.append(ppane);
      $('#'+pid).animate({
        'bottom': 0,
        'opacity': 0
      }, _anim);

      console.log('CONTENT REINSERTED: #'+id);

      scroller.classify(config.scroller.frame);
      scroller.jump(id);
    }
  }
};


$.fn.cms = function(method) {

    if (methods[method])
    {
      return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
    }
    else if (typeof method === 'object' || !method)
    {
      return methods.init.apply(this, arguments);
    }
    else
    {
      $.error('Method ' + method + ' does not exist on the selected object.');
    }

};

})(jQuery, window, document);