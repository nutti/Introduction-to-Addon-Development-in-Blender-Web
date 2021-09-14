function _open_pc_toc($) {
    $('.toc-pc').removeClass('pc-toc-closed');
    $('.body').removeClass('pc-toc-closed');
    $('#toggle-pc-toc-open').fadeOut(0);
    $('#toggle-pc-toc-close').fadeIn(0);
}

function _close_pc_toc($) {
    $('.toc-pc').addClass('pc-toc-closed');
    $('.body').addClass('pc-toc-closed');
    $('#toggle-pc-toc-open').fadeIn(0);
    $('#toggle-pc-toc-close').fadeOut(0);
}

function _open_sp_toc($) {
    $('.toc-sp').fadeIn(500);
    $('#toggle-sp-toc-open').fadeOut(0);
    $('.toggle-sp-toc-close').fadeIn(500);
}

function _close_sp_toc($) {
    $('.toc-sp').fadeOut(500);
    $('#toggle-sp-toc-open').fadeIn(500);
    $('.toggle-sp-toc-close').fadeOut(500);
}

function setupMenuVisibility()
{
    jQuery(function($) {
        if (localStorage.getItem('pc-toc-status')) {
            if (localStorage['pc-toc-status'] == 'opened') {
                _open_pc_toc($);
            } else if (localStorage['pc-toc-status'] == 'closed') {
                console.log("True");
                _close_pc_toc($);
            }
        }
    });
}

function toggleMenuVisibility()
{
    jQuery(function($) {
        $('a[href^="#"]').click(function() {
            var elem = $(this);
            var href = elem.attr('href');

            if (href == '#toggle-sp-toc-open') {
                _open_sp_toc($);
            }
            else if (href == '#toggle-sp-toc-close') {
                _close_sp_toc($);
            }
            else if (href == '#toggle-pc-toc-open') {
                _open_pc_toc($);
                localStorage['pc-toc-status'] = 'opened';
            }
            else if (href == '#toggle-pc-toc-close') {
                _close_pc_toc($);
                localStorage['pc-toc-status'] = 'closed';
            }
        });
    });
}

function enhanceCurrentTocItem()
{
    function enhance(tocId) {
        var toc = document.getElementById(tocId);
        if (toc == undefined) {
            return undefined;
        }
        var elements = toc.getElementsByTagName("*");
    
        var enhanceTarget = undefined;
        for (var i = 0; i < elements.length; ++i) {
            var elem = elements[i];
            for (var j = 0; j < elem.attributes.length; ++j) {
                var chapter = elem.attributes['toc-chapter'];
                var section = elem.attributes['toc-section'];
    
                if (chapter == undefined || chapter.value != targetChapter) {
                    continue;
                }
                if (section == undefined || section.value != targetSection) {
                    continue;
                }
    
                enhanceTarget = elem;
                break;
            }
        }
        if (enhanceTarget == undefined) {
            return undefined;
        }
    
        var targetPosition = enhanceTarget.getBoundingClientRect().top - window.innerHeight / 2;
        toc.scrollTo(0, targetPosition);
    
        enhanceTarget.classList.add('current');

        return enhanceTarget;
    }

    var params = (new URL(document.location)).searchParams;

    var targetChapter = params.get('toc-chapter');
    var targetSection = params.get('toc-section');

    tocList = ['toc-pc', 'toc-sp'];

    var targetList = [];
    for (var i = 0; i < tocList.length; ++i) {
        targetList.push(enhance(tocList[i]));
    }

    return targetList;
}

function addLinkHoverEffect()
{
    jQuery(function($) {
        var bodyContent = $('.body');
        bodyContent.find('a').mouseenter(function() {
            $(this).addClass('on');        
        })
        .mouseleave(function() {
            $(this).removeClass('on');
        });
    });
}
