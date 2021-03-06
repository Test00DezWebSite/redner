import pyredner
import torch

class Shape:
    def __init__(self, vertices, indices, uvs, normals, material_id):
        assert(vertices.dtype == torch.float32)
        assert(indices.dtype == torch.int32)
        assert(vertices.is_contiguous())
        assert(indices.is_contiguous())
        if (uvs is not None):
            assert(uvs.dtype == torch.float32)
            assert(uvs.is_contiguous())
        if (normals is not None):
            assert(normals.dtype == torch.float32)
            assert(normals.is_contiguous())
        if pyredner.get_use_gpu():
            assert(vertices.is_cuda)
            assert(indices.is_cuda)        
            assert(uvs is None or uvs.is_cuda)
            assert(normals is None or normals.is_cuda)
        else:
            assert(not vertices.is_cuda)
            assert(not indices.is_cuda)        
            assert(uvs is None or not uvs.is_cuda)
            assert(normals is None or not normals.is_cuda)

        self.vertices = vertices
        self.indices = indices
        self.uvs = uvs
        self.normals = normals
        self.material_id = material_id
        self.light_id = -1
