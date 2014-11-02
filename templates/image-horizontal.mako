<%inherit file="/site.mako" />
<%def name="title()">${c.dir.relative_path_parts()[-1][0]}: ${c.image.name}</%def>

##${h.link_to(c.dir.relative_path_parts()[-1][0], '/'+c.dir.relative_path_parts()[-1][1]+'/')}
${h.link_to(c.dir.relative_path_parts()[-1][0], c.dir.custom_relative_path('/dir') )}

<div class="row">
  <span class="description">
    ${h.link_to("^", c.dir.custom_relative_path('/dir'))} <br>
    ${h.link_to("^", c.dir.custom_relative_path('/dir'))} <br>
    ${h.link_to("^", c.dir.custom_relative_path('/dir'))} <br>
    ${h.link_to("^", c.dir.custom_relative_path('/dir'))} <br>
    
  </span>

  <span class="image">
    ${h.link_to(h.image(c.prev.get_size('tiny'), "<---"), c.prev.custom_relative_path("/image"), accesskey="a")}<br>
  </span>
							  
  <span class="selected">
    ${h.image(c.image.get_size('tiny'), c.image.ctime)}
  </span>

    % if c.admin:
  <span class="image">
    + -><br>
    - -><br>
  </span>
  <span class="image">
    ${h.link_to(h.image(c.next.get_size('tiny'), "  ->"), c.next.custom_relative_path("/image"), accesskey="d")}<br>
  </span>

    % else:
  <span class="image">
    ${h.link_to(h.image(c.next.get_size('tiny'), "  ->"), c.next.custom_relative_path("/image"), accesskey="d")}<br>
  </span>
    % endif

    % for i in c.nexts:
  <span class="image">
    ${h.link_to(h.image(i.get_size('tiny'), i.ctime), i.custom_relative_path("/image"))}<br>
  </span>
  % endfor

</div>

<div class="row">
<span class="image"> 
  % if c.link_full:
  ${h.link_to(h.image(c.image.get_size('large'), c.image.ctime), c.image.custom_relative_path(prefix='/file'))}
  % else:
  ${h.image(c.image.get_size('large'), c.image.ctime)}
  % endif
</span>
</div>

