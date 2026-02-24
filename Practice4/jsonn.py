import json

with open('sample.json') as f:
    data = json.load(f)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)


for item in data['imdata']:
    attr = item['l1PhysIf']['attributes']
    dn = attr.get('dn', '')
    desc = attr.get('descr', '')
    speed = attr.get('speed', 'inherit')
    mtu = attr.get('mtu', '')
    

    print(f"{dn:<50} {desc:<20} {speed:<7} {mtu:<6}")