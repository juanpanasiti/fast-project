import subprocess


def get_latest_git_tag() -> str:
    try:
        latest_commit = subprocess.check_output(
            ['git', 'rev-list', '--tags', '--max-count=1'],
            text=True
        ).strip()
        latest_tag = subprocess.check_output(
            ['git', 'describe', '--tags', latest_commit],
            text=True
        ).strip()
        return latest_tag
    except:
        return 'v0.0.1'


api_description = {
    'title': 'Fast-Projects',
    'description': 'Proyecto base del módulo de FastAPI del curso de Python+FastAPI.',
    'version': get_latest_git_tag(),
}
