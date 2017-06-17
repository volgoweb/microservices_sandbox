from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.App(__name__, port=5002, specification_dir='swagger/')
    app.add_api('api.yaml', resolver=RestyResolver('api'))
    app.run()
