from sqlalchemy.ext.declarative import DeclarativeMeta
import json
import datetime



def json_encoder(revisit_self = False, fields_to_expand = []):
    _visited_objs = []
    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                if revisit_self:
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    if isinstance(obj.__getattribute__(field), datetime.date):
                        val = str(obj.__getattribute__(field))
                    else:
                        val = obj.__getattribute__(field)
                    if isinstance(val.__class__, DeclarativeMeta) or (isinstance(val, list) and len(val) > 0 and isinstance(val[0].__class__, DeclarativeMeta)):
                        if field not in fields_to_expand:
                            fields[field] = None
                            continue
                    fields[field] = val
                return fields
            return json.JSONEncoder.default(self, obj)
    return AlchemyEncoder