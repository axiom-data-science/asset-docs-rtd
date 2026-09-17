from docutils import nodes
from docutils.parsers.rst import Directive, directives

gitlab_card_template = '''
<a class="gitlab-link" href="{gitlab_url}">
  <div class="gitlab-card">
      <img class="gitlab-project-avatar" width="80px" src="{avatar_url}" alt="project avatar" />
      <div class="description-container">
         <div class="gitlab-project-name">{name}</div>
         <div class="gitlab-project-description">{description}</div>
     </div>
  </div>
</a>
'''


class GitlabCard(Directive):
    option_spec = {
        'gitlab_url': directives.unchanged_required,
        'name': directives.unchanged_required,
        'description': directives.unchanged_required,
        'avatar_url': directives.unchanged,
    }

    def run(self):
        opts = self.options.copy()
        opts['avatar_url'] = opts.get('avatar_url', None) or '/_static/images/GitLab_logo-sq.png'

        html = gitlab_card_template.format(**opts)
        paragraph_node = nodes.raw('', html, format='html')
        return [paragraph_node]


def setup(app):
    app.add_directive("gitlab_card", GitlabCard)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
