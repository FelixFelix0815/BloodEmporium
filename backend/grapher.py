import networkx as nx

from backend.cvimage import CVImage
from graph_node import GraphNode
from shapes import UnmatchedNode, Connection


class Grapher:
    def __init__(self, circles: [UnmatchedNode], connections: [Connection]):
        self.circles = circles
        self.connections = connections

    def create(self):
        nodes = []
        ids = {}

        i = 1
        for circle in self.circles:
            if circle.unique_id == "ORIGIN":
                ids[circle] = "ORIGIN"
                nodes.append(GraphNode("ORIGIN", circle.unique_id, 9999, circle.xy(), True, True).get_tuple())
                continue

            node_id = f"{i}_{circle.unique_id}"
            ids[circle] = node_id
            is_accessible, is_user_claimed = GraphNode.state_from_color(circle.color)
            nodes.append(GraphNode(node_id, circle.unique_id, 9999, circle.xy(), is_accessible, is_user_claimed).get_tuple())
            i += 1

        # actual edges joining circles
        edges = []
        for connection in self.connections:
            edges.append((ids[connection.circle1], ids[connection.circle2]))

        # construct networkx graph
        graph = nx.Graph()
        graph.add_nodes_from(nodes)
        graph.add_edges_from(edges)
        return graph

    @staticmethod
    def update(base_bloodweb, updated_cv_image: CVImage, res):
        pass
        '''
        image_bgr = updated_cv_image.get_bgr()
        image_gray = updated_cv_image.get_gray()
        image_filtered = cv2.convertScaleAbs(image_gray, alpha=1.4, beta=0)
        image_filtered = cv2.fastNlMeansDenoising(image_filtered, None, 3, 7, 21)
        # image_filtered = cv2.GaussianBlur(image_filtered, (self.res.gaussian_c(),
        #                                   self.res.gaussian_c()), sigmaX=0, sigmaY=0)
        # image_filtered = cv2.bilateralFilter(image_filtered, self.res.bilateral_c(), 200, 200)

        to_remove = []
        for node_id, data in base_bloodweb.nodes.items():
            if data["is_user_claimed"]:
                # the one the user just claimed is handled previously in the main method
                continue
            r, color, match_unique_id = Matcher.get_circle_properties(None, image_gray, image_bgr, image_filtered, None,
                                                                      Position(int(data["x"]), int(data["y"])), res)
            if all(x is None for x in (r, color, match_unique_id)):
                # consumed by entity
                to_remove.append(node_id)
            else:
                # became available
                is_accessible, is_user_claimed = Node.state_from_color(color)
                nx.set_node_attributes(base_bloodweb, Node.from_dict(data, is_accessible=is_accessible,
                                                                     is_user_claimed=is_user_claimed).get_dict())

        for node_id in to_remove:
            base_bloodweb.remove_node(node_id)
        '''
