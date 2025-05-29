from typing import List, Callable, Dict, Set, Optional
from dataclasses import dataclass
import random

# === Step 1: Define a deadcode spec structure ===
@dataclass
class DeadcodeSpec:
    name: str
    generator: Callable[..., List[str]]
    allowed_contexts: Set[str]

# === Step 2: Deadcode Registry ===
class DeadcodeRegistry:
    def __init__(self):
        self.registry: Dict[str, DeadcodeSpec] = {}

    def register(self, name: str, generator: Callable[..., List[str]], contexts: Set[str]):
        self.registry[name] = DeadcodeSpec(name, generator, contexts)

    def get_random(self, context: str) -> Optional[DeadcodeSpec]:
        candidates = [spec for spec in self.registry.values() if context in spec.allowed_contexts]
        return random.choice(candidates) if candidates else None

# === Step 3: Global registry instance ===
registry = DeadcodeRegistry()

# === Step 4: Register built-in deadcode types ===
from qsharp_generator.deadcode import make_fixed_apply_if_equalle_block

registry.register(
    name="fixed_apply_if_equalle",
    generator=make_fixed_apply_if_equalle_block,
    contexts={"block", "inside-loop"}
)

# === Step 5: Helper to use from block generators ===
def insert_random_deadcode_block(
    context: str,
    target_register: str,
    target_indices: List[int],
    depth: int,
    builtin_block_names: List[str],
    required_imports: Set[str],
    make_if_block_adapter: Callable[[List[int]], Optional[Dict[str, any]]],
) -> Optional[List[str]]:
    spec = registry.get_random(context)
    if not spec:
        return None
    return spec.generator(
        target_register=target_register,
        target_indices=target_indices,
        depth=depth,
        builtin_block_names=builtin_block_names,
        required_imports=required_imports,
        make_if_block_adapter=make_if_block_adapter
    )
