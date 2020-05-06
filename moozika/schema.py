import graphene
import api.schema as api


class Query(api.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
