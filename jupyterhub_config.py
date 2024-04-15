from oauthenticator.generic import GenericOAuthenticator

c.JupyterHub.authenticator_class = GenericOAuthenticator

#c.GenericOAuthenticator.oauth_callback_url = 'http://165.73.223.70:8000/hub/oauth_callback'
c.GenericOAuthenticator.client_id = 'jp'
c.GenericOAuthenticator.client_secret = 'BuuSEHpWx5I1x2c05ZWmSLOnQGaDjlI1'
#c.GenericOAuthenticator.oauth_callback_url = 'http://165.73.223.70:8000/hub/oauth_callback'
c.GenericOAuthenticator.authorize_url = 'http://165.73.223.70:8080/realms/sso-demo/protocol/openid-connect/auth'
c.GenericOAuthenticator.token_url = 'http://165.73.223.70:8080/realms/sso-demo/protocol/openid-connect/token'
c.GenericOAuthenticator.userdata_url = 'http://165.73.223.70:8080/realms/sso-demo/protocol/openid-connect/userinfo'
c.GenericOAuthenticator.userdata_params = {'state': 'state'}
c.GenericOAuthenticator.username_claim = 'preferred_username'
c.GenericOAuthenticator.userdata_method = 'GET'
c.GenericOAuthenticator.login_service = 'Keycloak'
c.GenericOAuthenticator.scope = ['openid', 'profile']
c.JupyterHub.redirect_to_server = True
#c.GenericOAuthenticator.enable_auth_state = True
c.GenericOAuthenticator.auto_login = True
c.JupyterHub.spawner_class = 'jupyterhub.spawner.SimpleLocalProcessSpawner'
c.GenericOAthenticator.admin_users={'sso'}
