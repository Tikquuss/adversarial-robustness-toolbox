"""
Module providing poisoning attacks under a common interface.
"""
from art.attacks.poisoning.backdoor_attack import PoisoningAttackBackdoor
from art.attacks.poisoning.poisoning_attack_svm import PoisoningAttackSVM
from art.attacks.poisoning.feature_collision_attack import FeatureCollisionAttack
from art.attacks.poisoning.adversarial_embedding_attack import PoisoningAttackAdversarialEmbedding
